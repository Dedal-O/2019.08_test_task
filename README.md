# 2019.08_test_task
### Небольшой проект по тестовому заданию от работодателя
#### Для ускорения работ настройки - минимальны. А именно здесь в репозитории указан простой secret_key и в качестве базы данных применена sqlite. 
#### Для начала работ достаточно:
 * скачать данный репозиторий, 
 * установить пакеты из файла requirements.txt, 
 * запустить миграции, создать супервользователя 
#### Затем рекомендуется через админку добавить по несколько объектов в списки:
* Городские Районы (применяется для Организаций)
* Категории Товаров (применяется для товаров в номенклатуре)
* Названия Товаров (применяется для товаров в номенклатуре)
* Товары в номенклатуре (базовый спиисок товаров, применяется для последующего заполнения товарных единиц в карточках организаций)
* Организации (можно сказать, центральная фигура данного проекта)
* Торговые сети (несколько организаций объединяются в единые торговые сети)
