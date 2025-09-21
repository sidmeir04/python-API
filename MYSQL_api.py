from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import pooling
from mysql.connector import Error
from SQL_connecter import *
import json

app = Flask(__name__)

db_config = {
    "host": "localhost",
    "user": "connector",
    "password": "password",
    "database": "adler_aphasia_center",
    "auth_plugin": "mysql_native_password"
}

# Create a connection pool
try:
    pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=32, **db_config)
    print("Database connection pool created successfully.")
except mysql.connector.Error as e:
    print(f"Error creating MySQL connection pool: {e}")
    pool = None

# Function to get a connection from the pool
def get_connection():
    if pool:
        return pool.get_connection()
    else:
        raise ConnectionError("No database connection pool available.")


@app.route('/get_contact', methods=['POST'])
def get_contact():
    data = request.get_json()
    result = get_functions.get_contact(
        connection=get_connection(),
        id=data.get('id', None),
        staff=data.get('staff', None),
        caller_name=data.get('caller_name', None),
        caller_email=data.get('caller_email', None),
        call_date=data.get('call_date', None),
        phone_number=data.get('phone_number', None),
        referral_type=data.get('referral_type', None),
        additional_notes=data.get('additional_notes', None),
        tour_scheduled=data.get('tour_scheduled', None),
        tour_not_scheduled_reason=data.get('tour_not_scheduled_reason', None),
        follow_up_date=data.get('follow_up_date', None),
    )
    return jsonify(result), 200

@app.route('/update_contact', methods=['POST'])
def update_contact():
    data = json.loads(request.get_json()[0])
    update_functions.update_contact(
        connection=get_connection(),
        id=data.get('id'),
        staff=data.get('staff', None),
        caller_name=data.get('caller_name', None),
        caller_email=data.get('caller_email', None),
        call_date=data.get('call_date', None),
        phone_number=data.get('phone_number', None),
        referral_type=data.get('referral_type', None),
        additional_notes=data.get('additional_notes', None),
        tour_scheduled=data.get('tour_scheduled', None),
        tour_not_scheduled_reason=data.get('tour_not_scheduled_reason', None),
        follow_up_date=data.get('follow_up_date', None),
    )
    return '', 200

@app.route('/insert_contact', methods=['POST'])
def insert_contact():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_contact(
        connection=get_connection(),
        staff=data.get('staff', None),
        caller_name=data.get('caller_name', None),
        caller_email=data.get('caller_email', None),
        call_date=data.get('call_date', None),
        phone_number=data.get('phone_number', None),
        referral_type=data.get('referral_type', None),
        additional_notes=data.get('additional_notes', None),
        tour_scheduled=data.get('tour_scheduled', None),
        tour_not_scheduled_reason=data.get('tour_not_scheduled_reason', None),
        follow_up_date=data.get('follow_up_date', None),
    )
    return str(id), 200

@app.route('/get_tour', methods=['POST'])
def get_tour():
    data = request.get_json()
    result = get_functions.get_tour(
        connection=get_connection(),
        id=data.get('id', None),
        tour_date=data.get('tour_date', None),
        attended=data.get('attended', None),
        no_join_reason=data.get('no_join_reason', None),
        clinicians=data.get('clinicians', None),
        attendees=data.get('attendees', None),
        interactions=data.get('interactions', None),
        strategies_used=data.get('strategies_used', None),
        aep_deadline=data.get('aep_deadline', None),
        joined_after=data.get('joined_after', None),
        likely_to_join=data.get('likely_to_join', None),
        additional_notes=data.get('additional_notes', None),
        canceled=data.get('canceled', None),
        cancel_reason=data.get('cancel_reason', None),
    )
    return jsonify(result), 200

@app.route('/update_tour', methods=['POST'])
def update_tour():
    data = json.loads(request.get_json()[0])
    update_functions.update_tour(
        connection=get_connection(),
        id=data.get('id'),
        tour_date=data.get('tour_date', None),
        attended=data.get('attended', None),
        no_join_reason=data.get('no_join_reason', None),
        clinicians=data.get('clinicians', None),
        attendees=data.get('attendees', None),
        interactions=data.get('interactions', None),
        strategies_used=data.get('strategies_used', None),
        aep_deadline=data.get('aep_deadline', None),
        joined_after=data.get('joined_after', None),
        likely_to_join=data.get('likely_to_join', None),
        additional_notes=data.get('additional_notes', None),
        canceled=data.get('canceled', None),
        cancel_reason=data.get('cancel_reason', None),
    )
    return '', 200

@app.route('/insert_tour', methods=['POST'])
def insert_tour():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_tour(
        connection=get_connection(),
        tour_date=data.get('tour_date', None),
        attended=data.get('attended', None),
        no_join_reason=data.get('no_join_reason', None),
        clinicians=data.get('clinicians', None),
        attendees=data.get('attendees', None),
        interactions=data.get('interactions', None),
        strategies_used=data.get('strategies_used', None),
        aep_deadline=data.get('aep_deadline', None),
        joined_after=data.get('joined_after', None),
        likely_to_join=data.get('likely_to_join', None),
        additional_notes=data.get('additional_notes', None),
        canceled=data.get('canceled', None),
        cancel_reason=data.get('cancel_reason', None),
    )
    return str(id), 200

@app.route('/get_membership_enrollment_form', methods=['POST'])
def get_membership_enrollment_form():
    data = request.get_json()
    result = get_functions.get_membership_enrollment_form(
        connection=get_connection(),
        id=data.get('id', None),
        sexual_orientation=data.get('sexual_orientation', None),
        race=data.get('race', None),
        income=data.get('income', None),
        living_status=data.get('living_status', None),
        grew_up=data.get('grew_up', None),
        occupations=data.get('occupations', None),
        prev_speech_therapy=data.get('prev_speech_therapy', None),
        other_therapy=data.get('other_therapy', None),
        hearing_loss=data.get('hearing_loss', None),
        hearing_aid=data.get('hearing_aid', None),
        aphasia_cause=data.get('aphasia_cause', None),
        aphasia_onset=data.get('aphasia_onset', None),
        brain_location=data.get('brain_location', None),
        medications=data.get('medications', None),
        filled_by=data.get('filled_by', None),
        completed_date=data.get('completed_date', None),
        patient_info=data.get('patient_info', None),
    )
    return jsonify(result), 200

@app.route('/update_membership_enrollment_form', methods=['POST'])
def update_membership_enrollment_form():
    data = json.loads(request.get_json()[0])
    update_functions.update_membership_enrollment_form(
        connection=get_connection(),
        id=data.get('id'),
        sexual_orientation=data.get('sexual_orientation', None),
        race=data.get('race', None),
        income=data.get('income', None),
        living_status=data.get('living_status', None),
        grew_up=data.get('grew_up', None),
        occupations=data.get('occupations', None),
        prev_speech_therapy=data.get('prev_speech_therapy', None),
        other_therapy=data.get('other_therapy', None),
        hearing_loss=data.get('hearing_loss', None),
        hearing_aid=data.get('hearing_aid', None),
        aphasia_cause=data.get('aphasia_cause', None),
        aphasia_onset=data.get('aphasia_onset', None),
        brain_location=data.get('brain_location', None),
        medications=data.get('medications', None),
        filled_by=data.get('filled_by', None),
        completed_date=data.get('completed_date', None),
        patient_info=data.get('patient_info', None),
    )
    return '', 200

@app.route('/insert_membership_enrollment_form', methods=['POST'])
def insert_membership_enrollment_form():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_membership_enrollment_form(
        connection=get_connection(),
        sexual_orientation=data.get('sexual_orientation', None),
        race=data.get('race', None),
        income=data.get('income', None),
        living_status=data.get('living_status', None),
        grew_up=data.get('grew_up', None),
        occupations=data.get('occupations', None),
        prev_speech_therapy=data.get('prev_speech_therapy', None),
        other_therapy=data.get('other_therapy', None),
        hearing_loss=data.get('hearing_loss', None),
        hearing_aid=data.get('hearing_aid', None),
        aphasia_cause=data.get('aphasia_cause', None),
        aphasia_onset=data.get('aphasia_onset', None),
        brain_location=data.get('brain_location', None),
        medications=data.get('medications', None),
        filled_by=data.get('filled_by', None),
        completed_date=data.get('completed_date', None),
        patient_info=data.get('patient_info', None),
    )
    return str(id), 200

@app.route('/get_medical_history_form', methods=['POST'])
def get_medical_history_form():
    data = request.get_json()
    result = get_functions.get_medical_history_form(
        connection=get_connection(),
        id=data.get('id', None),
        physician_name=data.get('physician_name', None),
        specialty=data.get('specialty', None),
        physician_address=data.get('physician_address', None),
        physician_phone=data.get('physician_phone', None),
        aphasia_cause=data.get('aphasia_cause', None),
        aphasia_onset=data.get('aphasia_onset', None),
        stroke_location=data.get('stroke_location', None),
        lesion_location=data.get('lesion_location', None),
        primary_diagnosis=data.get('primary_diagnosis', None),
        secondary_diagnosis=data.get('secondary_diagnosis', None),
        seizure_history=data.get('seizure_history', None),
        last_seizure_date=data.get('last_seizure_date', None),
        anti_seizure_med=data.get('anti_seizure_med', None),
        visual_impairments=data.get('visual_impairments', None),
        visual_field_cut=data.get('visual_field_cut', None),
        other_visual_impairments=data.get('other_visual_impairments', None),
        completion_date=data.get('completion_date', None),
        other_conditions=data.get('other_conditions', None),
    )
    return jsonify(result), 200

@app.route('/update_medical_history_form', methods=['POST'])
def update_medical_history_form():
    data = json.loads(request.get_json()[0])
    update_functions.update_medical_history_form(
        connection=get_connection(),
        id=data.get('id'),
        physician_name=data.get('physician_name', None),
        specialty=data.get('specialty', None),
        physician_address=data.get('physician_address', None),
        physician_phone=data.get('physician_phone', None),
        aphasia_cause=data.get('aphasia_cause', None),
        aphasia_onset=data.get('aphasia_onset', None),
        stroke_location=data.get('stroke_location', None),
        lesion_location=data.get('lesion_location', None),
        primary_diagnosis=data.get('primary_diagnosis', None),
        secondary_diagnosis=data.get('secondary_diagnosis', None),
        seizure_history=data.get('seizure_history', None),
        last_seizure_date=data.get('last_seizure_date', None),
        anti_seizure_med=data.get('anti_seizure_med', None),
        visual_impairments=data.get('visual_impairments', None),
        visual_field_cut=data.get('visual_field_cut', None),
        other_visual_impairments=data.get('other_visual_impairments', None),
        completion_date=data.get('completion_date', None),
        other_conditions=data.get('other_conditions', None),
    )
    return '', 200

@app.route('/insert_medical_history_form', methods=['POST'])
def insert_medical_history_form():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_medical_history_form(
        connection=get_connection(),
        physician_name=data.get('physician_name', None),
        specialty=data.get('specialty', None),
        physician_address=data.get('physician_address', None),
        physician_phone=data.get('physician_phone', None),
        aphasia_cause=data.get('aphasia_cause', None),
        aphasia_onset=data.get('aphasia_onset', None),
        stroke_location=data.get('stroke_location', None),
        lesion_location=data.get('lesion_location', None),
        primary_diagnosis=data.get('primary_diagnosis', None),
        secondary_diagnosis=data.get('secondary_diagnosis', None),
        seizure_history=data.get('seizure_history', None),
        last_seizure_date=data.get('last_seizure_date', None),
        anti_seizure_med=data.get('anti_seizure_med', None),
        visual_impairments=data.get('visual_impairments', None),
        visual_field_cut=data.get('visual_field_cut', None),
        other_visual_impairments=data.get('other_visual_impairments', None),
        completion_date=data.get('completion_date', None),
        other_conditions=data.get('other_conditions', None),
    )
    return str(id), 200

@app.route('/get_incident_report', methods=['POST'])
def get_incident_report():
    data = request.get_json()
    result = get_functions.get_incident_report(
        connection=get_connection(),
        id=data.get('id', None),
        incident_date=data.get('incident_date', None),
        incident_location=data.get('incident_location', None),
        persons_involved=data.get('persons_involved', None),
        description=data.get('description', None),
        action_taken=data.get('action_taken', None),
    )
    return jsonify(result), 200

@app.route('/update_incident_report', methods=['POST'])
def update_incident_report():
    data = json.loads(request.get_json()[0])
    update_functions.update_incident_report(
        connection=get_connection(),
        id=data.get('id'),
        incident_date=data.get('incident_date', None),
        incident_location=data.get('incident_location', None),
        persons_involved=data.get('persons_involved', None),
        description=data.get('description', None),
        action_taken=data.get('action_taken', None),
    )
    return '', 200

@app.route('/insert_incident_report', methods=['POST'])
def insert_incident_report():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_incident_report(
        connection=get_connection(),
        incident_date=data.get('incident_date', None),
        incident_location=data.get('incident_location', None),
        persons_involved=data.get('persons_involved', None),
        description=data.get('description', None),
        action_taken=data.get('action_taken', None),
    )
    return str(id), 200

@app.route('/get_evaluation', methods=['POST'])
def get_evaluation():
    data = request.get_json()
    result = get_functions.get_evaluation(
        connection=get_connection(),
        id=data.get('id', None),
        completed=data.get('completed', None),
        administerer=data.get('administerer', None),
        test_type=data.get('test_type', None),
        date_administered=data.get('date_administered', None),
    )
    return jsonify(result), 200

@app.route('/update_evaluation', methods=['POST'])
def update_evaluation():
    data = json.loads(request.get_json()[0])
    update_functions.update_evaluation(
        connection=get_connection(),
        id=data.get('id'),
        completed=data.get('completed', None),
        administerer=data.get('administerer', None),
        test_type=data.get('test_type', None),
        date_administered=data.get('date_administered', None),
    )
    return '', 200

@app.route('/insert_evaluation', methods=['POST'])
def insert_evaluation():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_evaluation(
        connection=get_connection(),
        completed=data.get('completed', None),
        administerer=data.get('administerer', None),
        test_type=data.get('test_type', None),
        date_administered=data.get('date_administered', None),
    )
    return str(id), 200

@app.route('/get_transportation_information', methods=['POST'])
def get_transportation_information():
    data = request.get_json()
    result = get_functions.get_transportation_information(
        connection=get_connection(),
        id=data.get('id', None),
        am_name=data.get('am_name', None),
        am_phone=data.get('am_phone', None),
        pm_name=data.get('pm_name', None),
        pm_phone=data.get('pm_phone', None),
        transportation_notes=data.get('transportation_notes', None),
    )
    return jsonify(result), 200

@app.route('/update_transportation_information', methods=['POST'])
def update_transportation_information():
    data = json.loads(request.get_json()[0])
    update_functions.update_transportation_information(
        connection=get_connection(),
        id=data.get('id'),
        am_name=data.get('am_name', None),
        am_phone=data.get('am_phone', None),
        pm_name=data.get('pm_name', None),
        pm_phone=data.get('pm_phone', None),
        transportation_notes=data.get('transportation_notes', None),
    )
    return '', 200

@app.route('/insert_transportation_information', methods=['POST'])
def insert_transportation_information():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_transportation_information(
        connection=get_connection(),
        am_name=data.get('am_name', None),
        am_phone=data.get('am_phone', None),
        pm_name=data.get('pm_name', None),
        pm_phone=data.get('pm_phone', None),
        transportation_notes=data.get('transportation_notes', None),
    )
    return str(id), 200

@app.route('/get_emergency_contact', methods=['POST'])
def get_emergency_contact():
    data = request.get_json()
    result = get_functions.get_emergency_contact(
        connection=get_connection(),
        id=data.get('id', None),
        name=data.get('name', None),
        relationship=data.get('relationship', None),
        day_phone=data.get('day_phone', None),
        evening_phone=data.get('evening_phone', None),
        cell_phone=data.get('cell_phone', None),
        email=data.get('email', None),
        address=data.get('address', None),
        completion_date=data.get('completion_date', None),
    )
    return jsonify(result), 200

@app.route('/update_emergency_contact', methods=['POST'])
def update_emergency_contact():
    data = json.loads(request.get_json()[0])
    update_functions.update_emergency_contact(
        connection=get_connection(),
        id=data.get('id'),
        name=data.get('name', None),
        relationship=data.get('relationship', None),
        day_phone=data.get('day_phone', None),
        evening_phone=data.get('evening_phone', None),
        cell_phone=data.get('cell_phone', None),
        email=data.get('email', None),
        address=data.get('address', None),
        completion_date=data.get('completion_date', None),
    )
    return '', 200

@app.route('/insert_emergency_contact', methods=['POST'])
def insert_emergency_contact():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_emergency_contact(
        connection=get_connection(),
        name=data.get('name', None),
        relationship=data.get('relationship', None),
        day_phone=data.get('day_phone', None),
        evening_phone=data.get('evening_phone', None),
        cell_phone=data.get('cell_phone', None),
        email=data.get('email', None),
        address=data.get('address', None),
        completion_date=data.get('completion_date', None),
    )
    return str(id), 200

@app.route('/get_member', methods=['POST'])
def get_member():
    data = request.get_json()
    result = get_functions.get_member(
        connection=get_connection(),
        id=data.get('id', None),
        name=data.get('name', None),
        dob=data.get('dob', None),
        email=data.get('email', None),
        aep_completion_date=data.get('aep_completion_date', None),
        join_date=data.get('join_date', None),
        schedule=data.get('schedule', None),
        phone=data.get('phone', None),
        address=data.get('address', None),
        county=data.get('county', None),
        gender=data.get('gender', None),
        veteran=data.get('veteran', None),
        joined=data.get('joined', None),
        caregiver_needed=data.get('caregiver_needed', None),
        adler_program=data.get('adler_program', None),
        member_type=data.get('member_type', None),
        date_changed=data.get('date_changed', None),
        notes=data.get('notes', None),
        member_info=data.get('member_info', None),
        enrollment_form=data.get('enrollment_form', None),
        medical_history=data.get('medical_history', None),
        emergency_contact_one=data.get('emergency_contact_one', None),
        emergency_contact_two=data.get('emergency_contact_two', None),
        transport_info=data.get('transport_info', None),
    )
    return jsonify(result), 200

@app.route('/update_member', methods=['POST'])
def update_member():
    data = json.loads(request.get_json()[0])
    update_functions.update_member(
        connection=get_connection(),
        id=data.get('id'),
        name=data.get('name', None),
        dob=data.get('dob', None),
        email=data.get('email', None),
        aep_completion_date=data.get('aep_completion_date', None),
        join_date=data.get('join_date', None),
        schedule=data.get('schedule', None),
        phone=data.get('phone', None),
        address=data.get('address', None),
        county=data.get('county', None),
        gender=data.get('gender', None),
        veteran=data.get('veteran', None),
        joined=data.get('joined', None),
        caregiver_needed=data.get('caregiver_needed', None),
        adler_program=data.get('adler_program', None),
        member_type=data.get('member_type', None),
        date_changed=data.get('date_changed', None),
        notes=data.get('notes', None),
        member_info=data.get('member_info', None),
        enrollment_form=data.get('enrollment_form', None),
        medical_history=data.get('medical_history', None),
        emergency_contact_one=data.get('emergency_contact_one', None),
        emergency_contact_two=data.get('emergency_contact_two', None),
        transport_info=data.get('transport_info', None),
    )
    return '', 200

@app.route('/insert_member', methods=['POST'])
def insert_member():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_member(
        connection=get_connection(),
        name=data.get('name', None),
        dob=data.get('dob', None),
        email=data.get('email', None),
        aep_completion_date=data.get('aep_completion_date', None),
        join_date=data.get('join_date', None),
        schedule=data.get('schedule', None),
        phone=data.get('phone', None),
        address=data.get('address', None),
        county=data.get('county', None),
        gender=data.get('gender', None),
        veteran=data.get('veteran', None),
        joined=data.get('joined', None),
        caregiver_needed=data.get('caregiver_needed', None),
        adler_program=data.get('adler_program', None),
        member_type=data.get('member_type', None),
        date_changed=data.get('date_changed', None),
        notes=data.get('notes', None),
        member_info=data.get('member_info', None),
        enrollment_form=data.get('enrollment_form', None),
        medical_history=data.get('medical_history', None),
        emergency_contact_one=data.get('emergency_contact_one', None),
        emergency_contact_two=data.get('emergency_contact_two', None),
        transport_info=data.get('transport_info', None),
    )
    return str(id), 200

@app.route('/get_applications', methods=['POST'])
def get_applications():
    data = request.get_json()
    result = get_functions.get_applications(
        connection=get_connection(),
        id=data.get('id', None),
        birthday=data.get('birthday', None),
        occupation=data.get('occupation', None),
        is_slp=data.get('is_slp', None),
        relevant_experience=data.get('relevant_experience', None),
        education=data.get('education', None),
        interests_skills_hobbies=data.get('interests_skills_hobbies', None),
        languages_spoken=data.get('languages_spoken', None),
        will_substitute=data.get('will_substitute', None),
        convicted_of_crime=data.get('convicted_of_crime', None),
        application_date=data.get('application_date', None),
    )
    return jsonify(result), 200

@app.route('/update_applications', methods=['POST'])
def update_applications():
    data = json.loads(request.get_json()[0])
    update_functions.update_applications(
        connection=get_connection(),
        id=data.get('id'),
        birthday=data.get('birthday', None),
        occupation=data.get('occupation', None),
        is_slp=data.get('is_slp', None),
        relevant_experience=data.get('relevant_experience', None),
        education=data.get('education', None),
        interests_skills_hobbies=data.get('interests_skills_hobbies', None),
        languages_spoken=data.get('languages_spoken', None),
        will_substitute=data.get('will_substitute', None),
        convicted_of_crime=data.get('convicted_of_crime', None),
        application_date=data.get('application_date', None),
    )
    return '', 200

@app.route('/insert_applications', methods=['POST'])
def insert_applications():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_applications(
        connection=get_connection(),
        birthday=data.get('birthday', None),
        occupation=data.get('occupation', None),
        is_slp=data.get('is_slp', None),
        relevant_experience=data.get('relevant_experience', None),
        education=data.get('education', None),
        interests_skills_hobbies=data.get('interests_skills_hobbies', None),
        languages_spoken=data.get('languages_spoken', None),
        will_substitute=data.get('will_substitute', None),
        convicted_of_crime=data.get('convicted_of_crime', None),
        application_date=data.get('application_date', None),
    )
    return str(id), 200

@app.route('/get_volunteer', methods=['POST'])
def get_volunteer():
    data = request.get_json()
    result = get_functions.get_volunteer(
        connection=get_connection(),
        id=data.get('id', None),
        name=data.get('name', None),
        phone=data.get('phone', None),
        address=data.get('address', None),
        email=data.get('email', None),
        referral_source=data.get('referral_source', None),
        background_check_date=data.get('background_check_date', None),
        video_watched_date=data.get('video_watched_date', None),
        emergency_contacts=data.get('emergency_contacts', None),
        media_release=data.get('media_release', None),
        confidentiality=data.get('confidentiality', None),
        training_level=data.get('training_level', None),
        resumue=data.get('resumue', None),
    )
    return jsonify(result), 200

@app.route('/update_volunteer', methods=['POST'])
def update_volunteer():
    data = json.loads(request.get_json()[0])
    update_functions.update_volunteer(
        connection=get_connection(),
        id=data.get('id'),
        name=data.get('name', None),
        phone=data.get('phone', None),
        address=data.get('address', None),
        email=data.get('email', None),
        referral_source=data.get('referral_source', None),
        background_check_date=data.get('background_check_date', None),
        video_watched_date=data.get('video_watched_date', None),
        emergency_contacts=data.get('emergency_contacts', None),
        media_release=data.get('media_release', None),
        confidentiality=data.get('confidentiality', None),
        training_level=data.get('training_level', None),
        resumue=data.get('resumue', None),
    )
    return '', 200

@app.route('/insert_volunteer', methods=['POST'])
def insert_volunteer():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_volunteer(
        connection=get_connection(),
        name=data.get('name', None),
        phone=data.get('phone', None),
        address=data.get('address', None),
        email=data.get('email', None),
        referral_source=data.get('referral_source', None),
        background_check_date=data.get('background_check_date', None),
        video_watched_date=data.get('video_watched_date', None),
        emergency_contacts=data.get('emergency_contacts', None),
        media_release=data.get('media_release', None),
        confidentiality=data.get('confidentiality', None),
        training_level=data.get('training_level', None),
        resumue=data.get('resumue', None),
    )
    return str(id), 200

@app.route('/get_caregiver', methods=['POST'])
def get_caregiver():
    data = request.get_json()
    result = get_functions.get_caregiver(
        connection=get_connection(),
        id=data.get('id', None),
        name=data.get('name', None),
        phone=data.get('phone', None),
        email=data.get('email', None),
        relationship=data.get('relationship', None),
        date_contacted=data.get('date_contacted', None),
        notes=data.get('notes', None),
        group_attending=data.get('group_attending', None),
        attending=data.get('attending', None),
        caregiver_type=data.get('caregiver_type', None),
        sex=data.get('sex', None),
        race=data.get('race', None),
        occupations=data.get('occupations', None),
        support_group=data.get('support_group', None),
        covid_vaccine_date=data.get('covid_vaccine_date', None),
        allergies=data.get('allergies', None),
        medications=data.get('medications', None),
        participation=data.get('participation', None),
        robly=data.get('robly', None),
        enrollment_form=data.get('enrollment_form', None),
        medical_history=data.get('medical_history', None),
        emergency_contact_one=data.get('emergency_contact_one', None),
        emergency_contact_two=data.get('emergency_contact_two', None),
        transport_info=data.get('transport_info', None),
        member_id=data.get('member_id', None),
    )
    return jsonify(result), 200

@app.route('/update_caregiver', methods=['POST'])
def update_caregiver():
    data = json.loads(request.get_json()[0])
    update_functions.update_caregiver(
        connection=get_connection(),
        id=data.get('id'),
        name=data.get('name', None),
        phone=data.get('phone', None),
        email=data.get('email', None),
        relationship=data.get('relationship', None),
        date_contacted=data.get('date_contacted', None),
        notes=data.get('notes', None),
        group_attending=data.get('group_attending', None),
        attending=data.get('attending', None),
        caregiver_type=data.get('caregiver_type', None),
        sex=data.get('sex', None),
        race=data.get('race', None),
        occupations=data.get('occupations', None),
        support_group=data.get('support_group', None),
        covid_vaccine_date=data.get('covid_vaccine_date', None),
        allergies=data.get('allergies', None),
        medications=data.get('medications', None),
        participation=data.get('participation', None),
        robly=data.get('robly', None),
        enrollment_form=data.get('enrollment_form', None),
        medical_history=data.get('medical_history', None),
        emergency_contact_one=data.get('emergency_contact_one', None),
        emergency_contact_two=data.get('emergency_contact_two', None),
        transport_info=data.get('transport_info', None),
        member_id=data.get('member_id', None),
    )
    return '', 200

@app.route('/insert_caregiver', methods=['POST'])
def insert_caregiver():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_caregiver(
        connection=get_connection(),
        name=data.get('name', None),
        phone=data.get('phone', None),
        email=data.get('email', None),
        relationship=data.get('relationship', None),
        date_contacted=data.get('date_contacted', None),
        notes=data.get('notes', None),
        group_attending=data.get('group_attending', None),
        attending=data.get('attending', None),
        caregiver_type=data.get('caregiver_type', None),
        sex=data.get('sex', None),
        race=data.get('race', None),
        occupations=data.get('occupations', None),
        support_group=data.get('support_group', None),
        covid_vaccine_date=data.get('covid_vaccine_date', None),
        allergies=data.get('allergies', None),
        medications=data.get('medications', None),
        participation=data.get('participation', None),
        robly=data.get('robly', None),
        enrollment_form=data.get('enrollment_form', None),
        medical_history=data.get('medical_history', None),
        emergency_contact_one=data.get('emergency_contact_one', None),
        emergency_contact_two=data.get('emergency_contact_two', None),
        transport_info=data.get('transport_info', None),
        member_id=data.get('member_id', None),
    )
    return str(id), 200

@app.route('/get_outreach', methods=['POST'])
def get_outreach():
    data = request.get_json()
    result = get_functions.get_outreach(
        connection=get_connection(),
        id=data.get('id', None),
        contacted_date=data.get('contacted_date', None),
        staff_contacted=data.get('staff_contacted', None),
        organization=data.get('organization', None),
        org_type=data.get('org_type', None),
        outreach_type=data.get('outreach_type', None),
        target_location=data.get('target_location', None),
        num_people=data.get('num_people', None),
        robly=data.get('robly', None),
        notes=data.get('notes', None),
    )
    return jsonify(result), 200

@app.route('/update_outreach', methods=['POST'])
def update_outreach():
    data = json.loads(request.get_json()[0])
    update_functions.update_outreach(
        connection=get_connection(),
        id=data.get('id'),
        contacted_date=data.get('contacted_date', None),
        staff_contacted=data.get('staff_contacted', None),
        organization=data.get('organization', None),
        org_type=data.get('org_type', None),
        outreach_type=data.get('outreach_type', None),
        target_location=data.get('target_location', None),
        num_people=data.get('num_people', None),
        robly=data.get('robly', None),
        notes=data.get('notes', None),
    )
    return '', 200

@app.route('/insert_outreach', methods=['POST'])
def insert_outreach():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_outreach(
        connection=get_connection(),
        contacted_date=data.get('contacted_date', None),
        staff_contacted=data.get('staff_contacted', None),
        organization=data.get('organization', None),
        org_type=data.get('org_type', None),
        outreach_type=data.get('outreach_type', None),
        target_location=data.get('target_location', None),
        num_people=data.get('num_people', None),
        robly=data.get('robly', None),
        notes=data.get('notes', None),
    )
    return str(id), 200
if __name__ == '__main__':
    app.run(debug=True)