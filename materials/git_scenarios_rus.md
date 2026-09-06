# Git-сценарии первого дня

Все команды выполняются локально. Начало истории по START_HERE.md уже создало ветку develop и метку day01-start. Не вызывай повторный git init и не перемещай стартовую метку.

## 1. Сохранить результат задания 1

```bash
git status
git add src/partner/memory.txt src/quest1.sh
git commit -m "Восстановлена память, сохранены команды"
```

Коммит фиксирует только добавленные через add изменения. Сообщение должно объяснять, что сделано. Не создавай пустые коммиты для количества.

## 2. Отдельная ветка для первых скриптов

```bash
git checkout develop
git checkout -b feature/first-scripts
```

После готовности hello.py:

```bash
git add src/hello.py
git commit -m "feature/first-scripts: приветствие и проверка ввода"
```

После готовности calc.py:

```bash
git add src/calc.py
git commit -m "feature/first-scripts: арифметика и особые входы"
```

Ветка — отдельная линия работы. Название в сообщении не создаёт ветку: её создаёт checkout -b. В сообщениях её собственных коммитов нужен префикс feature/first-scripts:.

## 3. Слияние без fast-forward

```bash
git checkout develop
git merge --no-ff feature/first-scripts -m "Слияние первых скриптов"
git log --graph --oneline --all
```

`--no-ff` создаёт отдельный merge-коммит с двумя родителями. Первый — прежний develop, второй — вершина сливаемой ветки. Имя feature/first-scripts не удаляй: оно переносится со сдачей. Продолжай задания 4–5 в develop и коммить содержательные этапы. Между коммитами не нужно ждать определённое время.

## 4. Что изменилось

```bash
git status
git diff
git log --oneline day01-start..develop
git show ХЕШ_КОММИТА
```

`day01-start..develop` исключает исходную историю и показывает работу после выдачи. `git show` показывает содержимое коммита, включая конкретные изменения строк. В клоне ветки сервера или bundle видны через `git branch -a` с префиксом origin/; локальная feature-ветка автоматически не появляется.

## 5. Передать результат без сервера

Когда develop готова и git status чист:

```bash
python3 tools/day1.py pack --out ../day01_submission
```

Команда использует Git bundle и включает develop, feature/first-scripts и day01-start. Сам bundle — не ZIP и не папка исходников; это переносимая история Git. Проверяющий может клонировать его локально:

```bash
git clone --branch develop submission.bundle project
```

Путь перед bundle разрешено менять. Путь с пробелами заключай в кавычки. Для восстановления HOWTO удобнее скопировать bundle в новую пустую папку и выполнить команду оттуда.

## 6. Практика на новой ветке

На защите используются новая копия и имя ветки из карточки. Команды те же: checkout -b, редактор, add, commit, повторное изменение и commit, checkout develop, merge --no-ff. Не копируй имя старой feature-ветки вместо нового. В объяснении покажи, где появилась ветка и почему у merge два родителя.

## 7. Когда Git ругается

| Сообщение | Что делать |
| --- | --- |
| not a git repository | Проверь pwd, перейди в папку проекта |
| nothing to commit | Посмотри git status: есть ли изменённые файлы, выполнен ли add |
| Please tell me who you are | Задай локально git config user.name и git config user.email; --global не нужен |
| already exists при checkout -b | Ветка создана; для переключения используй checkout без -b |
| would be overwritten | Сначала сохрани работу коммитом; не затирай файлы вслепую |
| Открылся редактор merge | Сохрани сообщение; можно заранее передать -m "текст" |
| Папка сдачи уже существует | До приёма используй новое имя папки; принятую сдачу не заменяй |

SSH и настройка GitLab для обязательного маршрута не нужны.
