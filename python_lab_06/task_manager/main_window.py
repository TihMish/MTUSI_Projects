from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)
        self.init_ui()
        self.connect_signals()
        self.update_counter()

    def init_ui(self):
        self.title_label = QLabel("Новая задача")
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.add_button = QPushButton("Добавить")
        self.task_list = QListWidget()
        self.delete_button = QPushButton("Удалить")
        self.clear_button = QPushButton("Очистить всё")
        self.done_button = QPushButton("Отметить выполненной")
        self.delete_done_button = QPushButton("Удалить выполненные")
        self.counter_label = QLabel()
        self.done_label = QLabel()

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.clear_button)

        done_layout = QHBoxLayout()
        done_layout.addWidget(self.done_button)
        done_layout.addWidget(self.delete_done_button)

        counters_layout = QHBoxLayout()
        counters_layout.addWidget(self.counter_label)
        counters_layout.addWidget(self.done_label)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(done_layout)
        main_layout.addLayout(counters_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.statusBar().showMessage("Готово к работе")

    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.clear_button.clicked.connect(self.clear_tasks)
        self.done_button.clicked.connect(self.toggle_done)
        self.delete_done_button.clicked.connect(self.delete_done_tasks)
        self.task_list.itemChanged.connect(self.on_item_changed)

    def add_task(self):
        text = self.task_input.text().strip()
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")
            return
        item = QListWidgetItem(text)
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        item.setCheckState(Qt.CheckState.Unchecked)
        self.task_list.addItem(item)
        self.task_input.clear()
        self.update_counter()
        self.statusBar().showMessage(f"Добавлена задача: {text}")

    def delete_task(self):
        selected = self.task_list.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления")
            return
        item = selected[0]
        answer = QMessageBox.question(
            self, "Подтверждение", f"Удалить задачу «{item.text()}»?"
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.takeItem(self.task_list.row(item))
            self.update_counter()
            self.statusBar().showMessage(f"Удалена задача: {item.text()}")

    def clear_tasks(self):
        if self.task_list.count() == 0:
            QMessageBox.information(self, "Информация", "Список задач уже пуст")
            return
        answer = QMessageBox.question(
            self, "Подтверждение", "Удалить все задачи?"
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.clear()
            self.update_counter()
            self.statusBar().showMessage("Список задач очищен")

    def toggle_done(self):
        selected = self.task_list.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу")
            return
        item = selected[0]
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)

    def on_item_changed(self, item):
        is_done = item.checkState() == Qt.CheckState.Checked
        font = item.font()
        if font.strikeOut() != is_done:
            font.setStrikeOut(is_done)
            item.setFont(font)
        self.update_counter()
        if is_done:
            self.statusBar().showMessage(f"Выполнена задача: {item.text()}")
        else:
            self.statusBar().showMessage(f"Задача снова активна: {item.text()}")

    def delete_done_tasks(self):
        if self.count_done() == 0:
            QMessageBox.information(self, "Информация", "Нет выполненных задач")
            return
        answer = QMessageBox.question(
            self, "Подтверждение", "Удалить все выполненные задачи?"
        )
        if answer == QMessageBox.StandardButton.Yes:
            for row in range(self.task_list.count() - 1, -1, -1):
                if self.task_list.item(row).checkState() == Qt.CheckState.Checked:
                    self.task_list.takeItem(row)
            self.update_counter()
            self.statusBar().showMessage("Выполненные задачи удалены")

    def count_done(self):
        done = 0
        for row in range(self.task_list.count()):
            if self.task_list.item(row).checkState() == Qt.CheckState.Checked:
                done = done + 1
        return done

    def update_counter(self):
        self.counter_label.setText(f"Количество задач: {self.task_list.count()}")
        self.done_label.setText(f"Выполнено: {self.count_done()}")
