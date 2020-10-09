"""This file contain all database queries"""  

def Get_user_work_area_id(id_user, cnxn):
    """Receive an id user and return an id work area"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT id_work_area FROM users WHERE id=?", id_user).fetchone()
    if row == None:
        return None
    else:
        id_work_area = row[0]
        return id_work_area

def Get_job_offer_area_id(id_job_offer,cnxn):
    """Receive an id job offer and return an id work area"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT id_work_area FROM work_area_jobs WHERE id_job_offer=?", id_job_offer).fetchone()
    if row == None:
        return None
    else:
        id_work_area = row[0]
        return id_work_area

def Get_work_area(id, cnxn, _type):
    """Receive an id work area and return the work area name. 
        Depending on where the request comes this function could take two flows, 
        if  the request comes of  job offer or  user"""  
    if _type == 'job_offer':
        id = Get_job_offer_area_id(id,cnxn)
    else : 
        id = Get_user_work_area_id(id, cnxn)
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT title FROM work_areas WHERE id=?", id ).fetchone()
    if row == None:
        return None
    else:
        work_area = row[0]
        return work_area


def Get_user_qualification(id_user,cnxn):
    """Receive an id user and return user's qualification """
    employee = Is_employee(id_user,cnxn)
    if employee == 1:
        id_employee = Get_employee_id(id_user,cnxn)
        qualification = Get_qualificatio_employee(id_employee, cnxn)
        if id_employee == None or qualification == None:
            return None
    else:
        id_employer = Get_employer_id(id_user,cnxn)
        qualification = Get_qualificatio_employer(id_employer, cnxn)
        if id_employer == None or qualification == None:
            return None
    return qualification


def Is_employee(id_user,cnxn):
    """Receive an id user and return 1 if user is employee or 0 if not"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT employee FROM users WHERE id=?", id_user).fetchone()
    if row == None:
        return None
    else:
        employee = row[0]
        return employee

def Is_employer(id_user,cnxn):
    """Receive an id user and return 1 if user is employer or 0 if not"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT employer FROM users WHERE id=?", id_user).fetchone()
    if row == None:
        return None
    else:
        employer = row[0]
        return employer

def Get_employee_id(id_user,cnxn):
    """Receive an id user and return an id employee"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT id FROM employees WHERE id_user=?", id_user).fetchone()
    if row == None:
        return None
    else:
        id_employee = row[0]
        return id_employee

def Get_employer_id(id_user,cnxn):
    """Receive an id user and return an id employer"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT id FROM employers WHERE id_user=?", id_user).fetchone()
    if row == None:
        return None
    else:
        id_employer = row[0]
        return id_employer


def Get_qualificatio_employer(id_user_employer, cnxn):
    """Receive an id employer and return his qualification"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT qualification FROM scores WHERE id_employer=?", id_user_employer).fetchone()
    if row == None:
        return None
    else:
        qualification = row[0]
        return qualification

def Get_qualificatio_employee(id_user_employee, cnxn):
    """Receive an id employee and return his qualification"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT qualification FROM scores WHERE id_employee=?", id_user_employee).fetchone()
    if row == None:
        return None
    else:
        qualification = row[0]
        return qualification

def Get_user_latitude(id_user, cnxn):
    """Receive an id user and return his latitude"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT latitude FROM users WHERE id=?", id_user).fetchone()
    if row == None:
        return None
    else:
        latitude = row[0]
        return latitude

def Get_user_longitude(id_user, cnxn):
    """Receive an id user and return his longitude"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT longitude FROM users WHERE id=?", id_user).fetchone()
    if row == None:
        return None
    else:
        longitude = row[0]
        return longitude

def Get_work_area_id(title_work_area, cnxn):
    """ Recive a work area name and return an id work area """
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT id FROM work_areas WHERE title=?",title_work_area).fetchone()
    if row == None:
       return None
    else:
        id_work_area = row[0]
        return  id_work_area


def Get_info_based_on_work_area(id_work_area, cnxn, type_):
    """Recive an id work area and return a list of users or 
       job offers that math with this id work area"""
    cursor = cnxn.cursor()
    users = []
    if id_work_area == None:
        return None
    if type_ == 'user':
        row = cursor.execute("SELECT id FROM users WHERE id_work_area =?", id_work_area).fetchall()
        for i in row:
            users.append(i[0])
    elif type_ == 'job_offer':
        row = cursor.execute("SELECT id_job_offer FROM work_area_jobs WHERE id_work_area =?", id_work_area).fetchall()
        for i in row:
            users.append(i[0])
    else: 
        return None
    return users
        
       