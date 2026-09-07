# Git: рабочие сценарии

URL репозитория и права команда получает на платформе; адреса в примерах — обозначения.

```sh
git clone АДРЕС_РЕПОЗИТОРИЯ project
cd project
git checkout -b develop
git push -u origin develop
git checkout -b role/bank
git status
git diff
git add src/bank.py
git commit -m "role/bank: разобрать записи банка"
git push -u origin role/bank
```

Если develop уже есть, используйте `git checkout develop`, затем `git pull`.
Настройте имя и почту своего аккаунта локально: `git config user.name "Имя"`,
`git config user.email "ПОЧТА_АККАУНТА"`. Не используйте чужую учётную запись.

## Интеграция

```sh
git checkout develop
git pull
git checkout role/bank
git merge develop
```

При конфликте откройте помеченные файлы. Уберите маркеры <<<<<<<, =======,
>>>>>>> и оставьте согласованный код. Запустите проверки, затем git add и commit.

```sh
git checkout develop
git merge --no-ff role/bank
git push
git log --oneline --graph --all
git rev-parse HEAD
```

Последняя команда даёт ID версии для сдачи и для ссылок в документах. Не делайте force-push
общей ветки. Слияния координирует Интегратор; исключите одновременное редактирование
одних строк без разговора. До отправки убедитесь, что remote содержит нужный commit.

## Посмотреть прежнюю версию, не трогая сдачу

```sh
git clone АДРЕС_РЕПОЗИТОРИЯ experiment-copy
cd experiment-copy
git checkout ИДЕНТИФИКАТОР_COMMIT
```

Это отдельная копия; сданная версия не меняется. Не переносите случайно новые
файлы в старую версию и не запускайте старый код на новом банке, не сказав об этом.
