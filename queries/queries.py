
def Get_user_work_area_id(id_user, cnxn):
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT id_work_area FROM users WHERE id=?", id_user).fetchone()
    id_work_area = row[0]
    return id_work_area

def Get_job_offer_area_id(id_job_offer,cnxn):
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT id_work_area FROM work_area_jobs WHERE id_job_offer=?", id_job_offer).fetchone()
    id_work_area = row[0]
    return id_work_area

def Get_work_area(id, cnxn, _type):
    if _type == 'job_offer':
        id = Get_job_offer_area_id(id,cnxn)
    else : 
        id = Get_user_work_area_id(id, cnxn)
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT title FROM work_areas WHERE id=?", id ).fetchone()
    work_area = row[0]
    return work_area


def Get_user_qualification(id_user,cnxn):
    employee = Is_employee(id_user,cnxn)
    if employee == 1:
        id_employee = Get_employee_id(id_user,cnxn)
        qualification = Get_qualificatio_employee(id_employee, cnxn)
    else:
        id_employer = Get_employer_id(id_user,cnxn)
        qualification = Get_qualificatio_employer(id_employer, cnxn)
    return qualification


def Is_employee(id_user,cnxn):
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT employee FROM users WHERE id=?", id_user).fetchone()
    employee = row[0]
    return employee

def Is_employer(id_user,cnxn):
    """me sobra"""
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT employer FROM users WHERE id=?", id_user).fetchone()
    employer = row[0]
    return employer

def Get_employee_id(id_user,cnxn):
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT id FROM employees WHERE id_user=?", id_user).fetchone()
    id_employee = row[0]
    return id_employee

def Get_employer_id(id_user,cnxn):
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT id FROM employers WHERE id_user=?", id_user).fetchone()
    id_employer = row[0]
    return id_employer


def Get_qualificatio_employer(id_user_employer, cnxn):
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT qualification FROM scores WHERE id_employer=?", id_user_employer).fetchone()
    qualification = row[0]
    return qualification

def Get_qualificatio_employee(id_user_employee, cnxn):
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT qualification FROM scores WHERE id_employee=?", id_user_employee).fetchone()
    qualification = row[0]
    return qualification

def Get_user_latitude(id_user, cnxn):
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT latitude FROM users WHERE id=?", id_user).fetchone()
    latitude = row[0]
    return latitude

def Get_user_longitude(id_user, cnxn):
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT longitude FROM users WHERE id=?", id_user).fetchone()
    longitude = row[0]
    return longitude
