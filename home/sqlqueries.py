import sqlite3
from django.db import connection
from prettytable import PrettyTable


cursor = connection.cursor()


bestiary_select_query = '''SELECT Bestiary.Bestiary_ID
FROM Bestiary
LEFT JOIN Author ON Bestiary.Bestiary_Author = Author.Author_ID
LEFT JOIN Armor ON Bestiary.Armor_ID = Armor.Armor_ID
WHERE
    (? IS NULL OR Bestiary.Bestiary_ID LIKE ?) AND
    (? IS NULL OR Bestiary.Size_ID = ?) AND
    (? IS NULL OR Bestiary.Species_ID = ?) AND
    (? IS NULL OR Bestiary.Worldview_ID = ?) AND
    (? IS NULL OR Bestiary.Danger = ?) AND
    (? IS NULL OR Bestiary.Language_ID = ?) AND
    (? IS NULL OR Bestiary.Habitat_ID = ?) AND
    (? IS NULL OR (Author.Name || ' ' || Author.Last_Name) = ?) AND
    (? IS NULL OR Bestiary.Hits = ?) AND
    (? IS NULL OR Bestiary.Armor_ID = ?) AND
    (? IS NULL OR Armor.Armor_Class = ?);
'''

spells_select_query = '''SELECT Spells.Spell_ID 
FROM Spells 
LEFT JOIN Archetypes ON Spells.Archetypes = Archetypes.Archetypes_ID 
LEFT JOIN Author ON Spells.Spell_Author = Author.Author_ID 
WHERE 
    (? IS NULL OR Spells.Spell_ID LIKE ?) AND 
    (? IS NULL OR Spells.Spell_Level = ?) AND 
    (? IS NULL OR Archetypes.Class = ?) AND 
    (? IS NULL OR Spells.School = ?) AND 
    (? IS NULL OR Spells.Archetypes = ?) AND 
    (? IS NULL OR (Author.Name || ' ' || Author.Last_Name) = ?);
    '''

items_select_query = '''SELECT Item_ID 
FROM Items 
LEFT JOIN Author ON Items.Item_Author = Author.Author_ID 
WHERE 
    (? IS NULL OR Item_ID LIKE ?) AND 
    (? IS NULL OR Item_Type = ?) AND 
    (? IS NULL OR Item_Rarity = ?) AND 
    (? IS NULL OR Item_Setting = ?) AND 
    (? IS NULL OR Item_Price = ?) AND 
    (? IS NULL OR (Author.Name || ' ' || Author.Last_Name) = ?);
'''


bestiary_insert_query = '''INSERT INTO Bestiary (Bestiary_ID, Size_ID, Species_ID, Speed, Worldview_ID, Danger, Bestiary_Author, Language_ID, Habitat_ID, Hits, Armor_ID, Characteristics, Resistance_Damage, Immunity_Damage, Skills, Description)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''

spells_insert_query = '''INSERT INTO Spells (Spell_ID, Spell_Level, School, Archetypes, Spell_Author, Time_Application, Distance, Duration, Components, Description)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

items_insert_query = '''INSERT INTO home_items (Item_ID, Item_Type_id, Item_Rarity, Item_Setting, Item_Author_id, Item_Price, Item_Description)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    '''


def set_to_format(tup):
    converted_values = tuple(None if val == 'None' else val for val in tup)
    duplicated_values = tuple(val for val in converted_values for _ in range(2))
    return duplicated_values

def bestiary_select(params):
    params = set_to_format(params)
    cursor.execute(bestiary_select_query, params)
    result = cursor.fetchall()

    table = PrettyTable()

    # Определение столбцов таблицы
    table.field_names = [description[0] for description in cursor.description]

    # Добавление строк в таблицу
    for row in result:
        table.add_row(row)

    # Вывод таблицы на экран
    print(table.get_string())

def spells_select(params):
    params = set_to_format(params)
    cursor.execute(spells_select_query, params)
    result = cursor.fetchall()

    table = PrettyTable()

    # Определение столбцов таблицы
    table.field_names = [description[0] for description in cursor.description]

    # Добавление строк в таблицу
    for row in result:
        table.add_row(row)

    # Вывод таблицы на экран
    print(table.get_string())

def items_select(params):
    params = set_to_format(params)
    cursor.execute(items_select_query, params)
    result = cursor.fetchall()

    table = PrettyTable()

    # Определение столбцов таблицы
    table.field_names = [description[0] for description in cursor.description]

    # Добавление строк в таблицу
    for row in result:
        table.add_row(row)

    # Вывод таблицы на экран
    print(table.get_string())


def bestiary_insert(params):
    try:
        cursor.execute(bestiary_insert_query, params)
        return True
    except sqlite3.Error:
        return False


def spells_insert(params):
    try:
        cursor.execute(spells_insert_query, params)
        return True
    except sqlite3.Error as e:
        print("Ошибка при удалении из базы данных:", str(e))
        return False


def items_insert(params):
    try:
        cursor.execute(items_insert_query, params)
        return True
    except sqlite3.Error:
        return False


def bestiary_delete(params):
    try:
        query = "DELETE FROM Bestiary WHERE "
        conditions = []
        values = []

        for key, value in params.items():
            if value != "":
                conditions.append(f"{key} = ?")
                values.append(value)

        if not conditions:
            return False

        conditions_clause = " AND ".join(conditions)
        query += conditions_clause

        cursor.execute(query, values)

        if cursor.rowcount > 0:
            return True
        else:
            return False
    except sqlite3.Error as e:
        return False



def spells_delete(params):
    try:
        query = "DELETE FROM Spells WHERE "
        conditions = []
        values = []

        for key, value in params.items():
            if value != "":
                conditions.append(f"{key} = ?")
                values.append(value)

        if not conditions:
            return False

        conditions_clause = " AND ".join(conditions)
        query += conditions_clause

        cursor.execute(query, values)

        if cursor.rowcount > 0:
            return True
        else:
            return False
    except sqlite3.Error as e:
        return False


def items_delete(params):
    try:
        query = "DELETE FROM Items WHERE "
        conditions = []
        values = []

        for key, value in params.items():
            if value != "":
                conditions.append(f"{key} = ?")
                values.append(value)

        if not conditions:
            return False

        conditions_clause = " AND ".join(conditions)
        query += conditions_clause

        cursor.execute(query, values)

        if cursor.rowcount > 0:
            return True
        else:
            return False
    except sqlite3.Error as e:
        return False