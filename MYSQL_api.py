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
    pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=25, **db_config)
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

# def get_caller(connection, staff_name='', caller_name='', caller_email = '', call_date=None, phone='', referral_type='', tour_scheduled=None, follow_up_date=None):
@app.route('/get_caller', methods=['POST'])
def get_caller():
    caller_data = request.get_json()
    caller = get_functions.get_caller(
        connection=get_connection(),
        id=caller_data.get('id', None),
        staff_name=caller_data.get('staff_name', ''),
        caller_name=caller_data.get('caller_name', ''),
        caller_email=caller_data.get('caller_email', ''),
        call_date=caller_data.get('call_date', None),
        phone=caller_data.get('phone', ''),
        referral_type=caller_data.get('referral_type', ''),
        tour_scheduled=caller_data.get('tour_scheduled', None),
        follow_up_date=caller_data.get('follow_up_date', None)
    )
    return jsonify(caller), 200

@app.route('/get_tour', methods=['POST'])
def get_tour():
    tour_data = request.get_json()
    tour = get_functions.get_tour(
        connection=get_connection(),
        id=tour_data.get('id', None),
        tour_date=tour_data.get('tour_date', None),
        attended=tour_data.get('attended', None),
        clinicians=tour_data.get('clinicians', ''),
        strategies_used=tour_data.get('strategies_used', None),
        aep_deadline=tour_data.get('aep_deadline', None),
        joined_after=tour_data.get('joined_after', None),
        likely_to_join=tour_data.get('likely_to_join', None),
        canceled=tour_data.get('canceled', None),
    )
    return jsonify(tour), 200

@app.route('/get_member', methods=['POST'])
def get_member():
    member_data = request.get_json()
    member = get_functions.get_member(
        connection=get_connection(),
        id=member_data.get('id', None),
        name=member_data.get('name', ''),
        age=member_data.get('age', None),
        dob=member_data.get('dob', None),
        email=member_data.get('email', ''),
        schedule=member_data.get('schedule', None),
        phone=member_data.get('phone', ''),
        address=member_data.get('address', ''),
        county=member_data.get('county', ''),
        gender=member_data.get('gender', ''),
        veteran=member_data.get('veteran', None),
        joined=member_data.get('joined', None),
        caregiver_needed=member_data.get('caregiver_needed', None),
        alder_program=member_data.get('alder_program', ''),
    )
    return jsonify(member), 200

@app.route('/get_membership_enrollment_form', methods=['POST'])
def get_membership_enrollment_form():
    membership_enrollment_form_data = request.get_json()
    membership_enrollment_form = get_functions.get_membership_enrollment_form(
        connection=get_connection(),
        id=membership_enrollment_form_data.get('id', None),
        sexual_orientation=membership_enrollment_form_data.get('sexual_orientation', ''),
        race=membership_enrollment_form_data.get('race', ''),
        income=membership_enrollment_form_data.get('income', None),
        living_status=membership_enrollment_form_data.get('living_status', None),
        grew_up=membership_enrollment_form_data.get('grew_up', ''),
        hearing_loss=membership_enrollment_form_data.get('hearing_loss', None),
        hearing_aid=membership_enrollment_form_data.get('hearing_aid', None),
        aphasia_cause=membership_enrollment_form_data.get('aphasia_cause', ''),
        aphasia_onset=membership_enrollment_form_data.get('aphasia_onset', None),
        brain_location=membership_enrollment_form_data.get('brain_location', ''),
        filled_by=membership_enrollment_form_data.get('filled_by', ''),
        completed_date=membership_enrollment_form_data.get('completed_date', None),
    )
    return jsonify(membership_enrollment_form), 200

@app.route('/get_medical_history_form', methods=['POST'])
def get_medical_history_form():
    medical_history_form_data = request.get_json()
    medical_history_form = get_functions.get_medical_history_form(
        connection=get_connection(),
        id=medical_history_form_data.get('id', None),
        physician_name=medical_history_form_data.get('physician_name', None),
        specialty=medical_history_form_data.get('specialty', None),
        physician_address=medical_history_form_data.get('physician_address', None),
        physician_phone=medical_history_form_data.get('physician_phone', None),
        aphasia_cause=medical_history_form_data.get('aphasia_cause', None),
        aphasia_onset=medical_history_form_data.get('aphasia_onset', None),
        stroke_location=medical_history_form_data.get('stroke_location', None),
        lesion_location=medical_history_form_data.get('lesion_location', None),
        primary_diagnosis=medical_history_form_data.get('primary_diagnosis', None),
        secondary_diagnosis=medical_history_form_data.get('secondary_diagnosis', None),
        seizure_history=medical_history_form_data.get('seizure_history', None),
        last_seizure_date=medical_history_form_data.get('last_seizure_date', None),
        anti_seizure_med=medical_history_form_data.get('anti_seizure_med', None),
        visual_impairments=medical_history_form_data.get('visual_impairments', None),
        visual_field_cut=medical_history_form_data.get('visual_field_cut', None),
        other_visual_impairments=medical_history_form_data.get('other_visual_impairments', None),
        completion_date=medical_history_form_data.get('completion_date', None),
    )
    return jsonify(medical_history_form), 200

@app.route('/get_incident_report', methods=['POST'])
def get_incident_report():
    incident_report_data = request.get_json()
    incident_report = get_functions.get_incident_report(
        connection=get_connection(),
        id=incident_report_data.get('id', None),
        incident_date=incident_report_data.get('incident_date', None),
        incident_location=incident_report_data.get('incident_location', ''),
    )
    return jsonify(incident_report), 200

@app.route('/get_evaluation', methods=['POST'])
def get_evaluation():
    evaluation_data = request.get_json()
    evaluation = get_functions.get_evaluation(
        connection=get_connection(),
        id=evaluation_data.get('id', None),
        completed=evaluation_data.get('completed', None),
        administerer=evaluation_data.get('administerer', ''),
        date_administered=evaluation_data.get('date_administered', None),
    )
    return jsonify(evaluation), 200

@app.route('/get_transportation_information', methods=['POST'])
def get_transportation_information():
    transportation_data = request.get_json()
    transportation_information = get_functions.get_transportation_information(
        connection=get_connection(),
        id=transportation_data.get('id', None),
        bus_transport=transportation_data.get('bus_transport', None),
        bus_company=transportation_data.get('bus_company', ''),
        bus_contact_phone=transportation_data.get('bus_contact_phone', ''),
        picked_up=transportation_data.get('picked_up', None),
        pickup_person=transportation_data.get('pickup_person', ''),
        relationship_to_member=transportation_data.get('relationship_to_member', ''),
        primary_phone=transportation_data.get('primary_phone', ''),
        secondary_phone=transportation_data.get('secondary_phone', ''),
    )
    return jsonify(transportation_information), 200

@app.route('/get_caregiver', methods=['POST'])
def get_caregiver():
    caregiver_data = request.get_json()
    print(caregiver_data)
    caregiver = get_functions.get_caregiver(
        connection=get_connection(),
        id=caregiver_data.get('id', None),
        name=caregiver_data.get('name', ''),
        phone=caregiver_data.get('phone', ''),
        email=caregiver_data.get('email', ''),
        relationship=caregiver_data.get('relationship', ''),
        date_contacted=caregiver_data.get('date_contacted', None),
        group_attending=caregiver_data.get('group_attending', ''),
        attending=caregiver_data.get('attending', None),
        caregiver_type=caregiver_data.get('caregiver_type', ''),
        sex=caregiver_data.get('sex', ''),
        race=caregiver_data.get('race', ''),
        occupations=caregiver_data.get('occupations', ''),
        support_group=caregiver_data.get('support_group', None),
        allergies=caregiver_data.get('allergies', ''),
        medications=caregiver_data.get('medications', ''),
        participation=caregiver_data.get('participation', ''),
        robly=caregiver_data.get('robly', None),
        enrollment_form=caregiver_data.get('enrollment_form', None),
        medical_history=caregiver_data.get('medical_history', None),
        emergency_contact_one=caregiver_data.get('emergency_contact_one', None),
        emergency_contact_two=caregiver_data.get('emergency_contact_two', None),
        transport_info=caregiver_data.get('transport_info', None),
        member_id=caregiver_data.get('member_id', None),
    )
    return jsonify(caregiver), 200

@app.route('/get_emergency_contact', methods=['POST'])
def get_emergency_contact():
    emergency_contact_data = request.get_json()
    emergency_contact = get_functions.get_emergency_contact(
        connection=get_connection(),
        id=emergency_contact_data.get('id', None),
        name=emergency_contact_data.get('name', ''),
        relationship=emergency_contact_data.get('relationship', ''),
        day_phone=emergency_contact_data.get('day_phone', ''),
        evening_phone=emergency_contact_data.get('evening_phone', ''),
        cell_phone=emergency_contact_data.get('cell_phone', ''),
        address=emergency_contact_data.get('address', ''),
        completion_date=emergency_contact_data.get('completion_date', None),
    )
    return jsonify(emergency_contact), 200

@app.route('/get_volunteer', methods=['POST'])
def get_volunteer():
    volunteer_data = request.get_json()
    volunteer = get_functions.get_volunteer(
        connection=get_connection(),
        id=volunteer_data.get('id', None),
        name=volunteer_data.get('name', ''),
        phone=volunteer_data.get('phone', ''),
        address=volunteer_data.get('address', ''),
        email=volunteer_data.get('email', ''),
        background_check_date=volunteer_data.get('background_check_date', None),
        video_watched_date=volunteer_data.get('video_watched_date', None),
        media_release=volunteer_data.get('media_release', None),
        confidentiality=volunteer_data.get('confidentiality', None),
        training_level=volunteer_data.get('training_level', None),
    )
    return jsonify(volunteer), 200

@app.route('/get_applications', methods=['POST'])
def get_applications():
    applications_data = request.get_json()
    applications = get_functions.get_applications(
        connection=get_connection(),
        id=applications_data.get('id', None),
        birthday=applications_data.get('birthday', None),
        occupation=applications_data.get('occupation', ''),
        is_slp=applications_data.get('is_slp', None),
        languages_spoken=applications_data.get('languages_spoken', ''),
        will_substitute=applications_data.get('will_substitute', None),
        convicted_of_crime=applications_data.get('convicted_of_crime', None),
        application_date=applications_data.get('application_date', None),
    )
    return jsonify(applications), 200

@app.route('/get_outreach', methods=['POST'])
def get_outreach():
    outreach_data = request.get_json()
    outreach = get_functions.get_outreach(
        connection=get_connection(),
        id=outreach_data.get('id', None),
        contacted_date=outreach_data.get('contacted_date', None),
        staff_contacted=outreach_data.get('staff_contacted', ''),
        organization=outreach_data.get('organization', ''),
        org_type=outreach_data.get('org_type', ''),
        outreach_type=outreach_data.get('outreach_type', ''),
        target_location=outreach_data.get('target_location', ''),
        num_people=outreach_data.get('num_people', None),
        robly=outreach_data.get('robly', None),
    )
    return jsonify(outreach), 200

@app.route('/update_caller', methods=['POST'])
def update_caller():
    caller_data = json.loads(request.get_json()[0])
    update_functions.update_caller(
        connection=get_connection(),
        id=caller_data.get('id'),
        staff=caller_data.get('staff', None),
        caller_name=caller_data.get('caller_name', None),
        caller_email=caller_data.get('caller_email', None),
        call_date=caller_data.get('call_date', None),
        phone_number=caller_data.get('phone_number', None),
        referral_type=caller_data.get('referral_type', None),
        additional_notes=caller_data.get('additional_notes', None),
        tour_scheduled=caller_data.get('tour_scheduled', None),
        tour_not_scheduled_reason=caller_data.get('tour_not_scheduled_reason', None),
        follow_up_date=caller_data.get('follow_up_date', None)
    )
    return '', 200

@app.route('/update_tour', methods=['POST'])
def update_tour():
    tour_data = json.loads(request.get_json()[0])
    update_functions.update_tour(
        connection=get_connection(),
        id=tour_data.get('id'),
        tour_date=tour_data.get('tour_date', None),
        attended=tour_data.get('attended', None),
        no_join_reason=tour_data.get('no_join_reason', None),
        clinicians=tour_data.get('clinicians', None),
        attendees=tour_data.get('attendees', None),
        interactions=tour_data.get('interactions', None),
        strategies_used=tour_data.get('strategies_used', None),
        aep_deadline=tour_data.get('aep_deadline', None),
        joined_after=tour_data.get('joined_after', None),
        likely_to_join=tour_data.get('likely_to_join', None),
        additional_notes=tour_data.get('additional_notes', None),
        canceled=tour_data.get('canceled', None),
        cancel_reason=tour_data.get('cancel_reason', None),
    )
    return '', 200

@app.route('/update_member', methods=['POST'])
def update_member():
    member_data = json.loads(request.get_json()[0])
    update_functions.update_member(
        connection=get_connection(),
        id=member_data.get('id'),
        name=member_data.get('name', None),
        age=member_data.get('age', None),
        dob=member_data.get('dob', None),
        email=member_data.get('email', None),
        aep_completion_date=member_data.get('aep_completion_date', None),
        join_date=member_data.get('join_date', None),
        schedule=member_data.get('schedule', None),
        phone=member_data.get('phone', None),
        address=member_data.get('address', None),
        county=member_data.get('county', None),
        gender=member_data.get('gender', None),
        veteran=member_data.get('veteran', None),
        joined=member_data.get('joined', None),
        caregiver_needed=member_data.get('caregiver_needed', None),
        alder_program=member_data.get('alder_program', None),
        medical_history=member_data.get('medical_history', None),
        emergency_contact_one=member_data.get('emergency_contact_one', None),
        emergency_contact_two=member_data.get('emergency_contact_two', None),
        enrollment_form=member_data.get('enrollment_form', None),
        notes=member_data.get('notes', None)
    )
    return '', 200

@app.route('/update_membership_enrollment_form', methods=['POST'])
def update_membership_enrollment_form():
    enrollment_form_data = json.loads(request.get_json()[0])
    update_functions.update_membership_enrollment_form(
        connection=get_connection(),
        # see update_emergency_contact for why this is a list
        id=enrollment_form_data.get('id')[0],
        sexual_orientation=enrollment_form_data.get('sexual_orientation', None),
        race=enrollment_form_data.get('race', None),
        income=enrollment_form_data.get('income', None),
        living_status=enrollment_form_data.get('living_status', None),
        grew_up=enrollment_form_data.get('grew_up', None),
        occupations=enrollment_form_data.get('occupations', None),
        prev_speech_therapy=enrollment_form_data.get('prev_speech_therapy', None),
        other_therapy=enrollment_form_data.get('other_therapy', None),
        hearing_loss=enrollment_form_data.get('hearing_loss', None),
        hearing_aid=enrollment_form_data.get('hearing_aid', None),
        aphasia_cause=enrollment_form_data.get('aphasia_cause', None),
        aphasia_onset=enrollment_form_data.get('aphasia_onset', None),
        brain_location=enrollment_form_data.get('brain_location', None),
        allergies=enrollment_form_data.get('allergies', None),
        medications=enrollment_form_data.get('medications', None),
        filled_by=enrollment_form_data.get('filled_by', None),
        completed_date=enrollment_form_data.get('completed_date', None),
        patient_info=json.dumps(enrollment_form_data.get('patient_info', None))
    )
    return '', 200

@app.route('/update_medical_history_form', methods=['POST'])
def update_medical_history_form():
    medical_history_data = json.loads(request.get_json()[0])
    update_functions.update_medical_history_form(
        connection=get_connection(),
        # see update_emergency_contact for why this is a list
        id=medical_history_data.get('id')[0],
        physician_name=medical_history_data.get('physician_name', None),
        specialty=medical_history_data.get('specialty', None),
        physician_address=medical_history_data.get('physician_address', None),
        physician_phone=medical_history_data.get('physician_phone', None),
        aphasia_cause=medical_history_data.get('aphasia_cause', None),
        aphasia_onset=medical_history_data.get('aphasia_onset', None),
        stroke_location=medical_history_data.get('stroke_location', None),
        lesion_location=medical_history_data.get('lesion_location', None),
        primary_diagnosis=medical_history_data.get('primary_diagnosis', None),
        secondary_diagnosis=medical_history_data.get('secondary_diagnosis', None),
        seizure_history=medical_history_data.get('seizure_history', None),
        last_seizure_date=medical_history_data.get('last_seizure_date', None),
        anti_seizure_med=medical_history_data.get('anti_seizure_med', None),
        visual_impairments=medical_history_data.get('visual_impairments', None),
        visual_field_cut=medical_history_data.get('visual_field_cut', None),
        other_visual_impairments=medical_history_data.get('other_visual_impairments', None),
        completion_date=medical_history_data.get('completion_date', None),
        other_medical_conditions=json.dumps(medical_history_data.get('other_medical_conditions', None))
    )
    return '', 200

@app.route('/update_incident_report', methods=['POST'])
def update_incident_report():
    incident_report_data = json.loads(request.get_json()[0])
    update_functions.update_incident_report(
        connection=get_connection(),
        id=incident_report_data.get('id'),
        incident_date=incident_report_data.get('incident_date', None),
        incident_location=incident_report_data.get('incident_location', None),
        persons_involved=incident_report_data.get('persons_involved', None),
        description=incident_report_data.get('description', None),
        action_taken=incident_report_data.get('action_taken', None),
    )
    return '', 200

@app.route('/update_evaluation', methods=['POST'])
def update_evaluation():
    evaluation_data = json.loads(request.get_json()[0])
    update_functions.update_evaluation(
        connection=get_connection(),
        id=evaluation_data.get('id'),
        completed=evaluation_data.get('completed', None),
        administerer=evaluation_data.get('administerer', None),
        test_type=evaluation_data.get('test_type', None),
        date_administered=evaluation_data.get('date_administered', None),
    )
    return '', 200

@app.route('/update_transportation_information', methods=['POST'])
def update_transportation_information():
    transportation_data = json.loads(request.get_json()[0])
    update_functions.update_transportation_information(
        connection=get_connection(),
        id=transportation_data.get('id'),
        bus_transport=transportation_data.get('bus_transport', None),
        bus_company=transportation_data.get('bus_company', None),
        bus_contact_phone=transportation_data.get('bus_contact_phone', None),
        picked_up=transportation_data.get('picked_up', None),
        pickup_person=transportation_data.get('pickup_person', None),
        relationship_to_member=transportation_data.get('relationship_to_member', None),
        primary_phone=transportation_data.get('primary_phone', None),
        secondary_phone=transportation_data.get('secondary_phone', None),
    )
    return '', 200

@app.route('/update_caregiver', methods=['POST'])
def update_caregiver():
    caregiver_data = json.loads(request.get_json()[0])
    update_functions.update_caregiver(
        connection=get_connection(),
        id=caregiver_data.get('id')[0],
        name=caregiver_data.get('name', None),
        phone=caregiver_data.get('phone', None),
        email=caregiver_data.get('email', None),
        relationship=caregiver_data.get('relationship', None),
        date_contacted=caregiver_data.get('date_contacted', None),
        notes=caregiver_data.get('notes', None),
        group_attending=caregiver_data.get('group_attending', None),
        attending=caregiver_data.get('attending', None),
        caregiver_type=caregiver_data.get('caregiver_type', None),
        sex=caregiver_data.get('sex', None),
        race=caregiver_data.get('race', None),
        occupations=caregiver_data.get('occupations', None),
        support_group=caregiver_data.get('support_group', None),
        covid_vaccine_date=caregiver_data.get('covid_vaccine_date', None),
        allergies=caregiver_data.get('allergies', None),
        medications=caregiver_data.get('medications', None),
        participation=caregiver_data.get('participation', None),
        robly=caregiver_data.get('robly', None),
        enrollment_form=caregiver_data.get('enrollment_form', None),
        medical_history=caregiver_data.get('medical_history', None),
        emergency_contact_one=caregiver_data.get('emergency_contact_one', None),
        emergency_contact_two=caregiver_data.get('emergency_contact_two', None),
        transport_info=caregiver_data.get('transport_info', None),
        member_id=caregiver_data.get('member_id', None),
    )
    return '', 200

@app.route('/update_emergency_contact', methods=['POST'])
def update_emergency_contact():
    emergency_contact_data = json.loads(request.get_json()[0])
    update_functions.update_emergency_contact(
        connection=get_connection(),
        # id should be given as list with only one item being the id
        # had to do this b/c of spagetti code on front end :)
        id=emergency_contact_data.get('id')[0],
        name=emergency_contact_data.get('name', None),
        relationship=emergency_contact_data.get('relationship', None),
        day_phone=emergency_contact_data.get('day_phone', None),
        evening_phone=emergency_contact_data.get('evening_phone', None),
        cell_phone=emergency_contact_data.get('cell_phone', None),
        email=emergency_contact_data.get('email', None),
        address=emergency_contact_data.get('address', None),
        completion_date=emergency_contact_data.get('completion_date', None),
    )
    return '', 200

@app.route('/update_volunteer', methods=['POST'])
def update_volunteer():
    volunteer_data = json.loads(request.get_json()[0])
    update_functions.update_volunteer(
        connection=get_connection(),
        id=volunteer_data.get('id'),
        name=volunteer_data.get('name', None),
        phone=volunteer_data.get('phone', None),
        address=volunteer_data.get('address', None),
        email=volunteer_data.get('email', None),
        referral_source=volunteer_data.get('referral_source', None),
        background_check_date=volunteer_data.get('background_check_date', None),
        video_watched_date=volunteer_data.get('video_watched_date', None),
        emergency_contacts=volunteer_data.get('emergency_contacts', None),
        media_release=volunteer_data.get('media_release', None),
        confidentiality=volunteer_data.get('confidentiality', None),
        training_level=volunteer_data.get('training_level', None),
    )
    return '', 200

@app.route('/update_applications', methods=['POST'])
def update_applications():
    application_data = json.loads(request.get_json()[0])
    update_functions.update_applications(
        connection=get_connection(),
        id=application_data.get('id'),
        birthday=application_data.get('birthday', None),
        occupation=application_data.get('occupation', None),
        is_slp=application_data.get('is_slp', None),
        relevant_experience=application_data.get('relevant_experience', None),
        education=application_data.get('education', None),
        interests_skills_hobbies=application_data.get('interests_skills_hobbies', None),
        languages_spoken=application_data.get('languages_spoken', None),
        will_substitute=application_data.get('will_substitute', None),
        convicted_of_crime=application_data.get('convicted_of_crime', None),
        application_date=application_data.get('application_date', None),
    )
    return '', 200

@app.route('/update_outreach', methods=['POST'])
def update_outreach():
    outreach_data = json.loads(request.get_json()[0])
    update_functions.update_outreach(
        connection=get_connection(),
        id=outreach_data.get('id'),
        contacted_date=outreach_data.get('contacted_date', None),
        staff_contacted=outreach_data.get('staff_contacted', None),
        organization=outreach_data.get('organization', None),
        org_type=outreach_data.get('org_type', None),
        outreach_type=outreach_data.get('outreach_type', None),
        target_location=outreach_data.get('target_location', None),
        num_people=outreach_data.get('num_people', None),
        robly=outreach_data.get('robly', None),
        notes=outreach_data.get('notes', None),
    )
    return '', 200

@app.route('/insert_caller', methods=['POST'])
def insert_caller():
    caller_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_caller(
        connection=get_connection(),
        staff=caller_data.get('staff', None),
        caller_name=caller_data.get('caller_name', None),
        caller_email=caller_data.get('caller_email', None),
        call_date=caller_data.get('call_date', None),
        phone_number=caller_data.get('phone_number', None),
        referral_type=caller_data.get('referral_type', None),
        additional_notes=caller_data.get('additional_notes', None),
        tour_scheduled=caller_data.get('tour_scheduled', None),
        tour_not_scheduled_reason=caller_data.get('tour_not_scheduled_reason', None),
        follow_up_date=caller_data.get('follow_up_date', None)
    )
    return str(id), 200

@app.route('/insert_tour', methods=['POST'])
def insert_tour():
    tour_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_tour(
        connection=get_connection(),
        tour_date=tour_data.get('tour_date', None),
        attended=tour_data.get('attended', None),
        no_join_reason=tour_data.get('no_join_reason', None),
        clinicians=tour_data.get('clinicians', None),
        attendees=tour_data.get('attendees', None),
        interactions=tour_data.get('interactions', None),
        strategies_used=tour_data.get('strategies_used', None),
        aep_deadline=tour_data.get('aep_deadline', None),
        joined_after=tour_data.get('joined_after', None),
        likely_to_join=tour_data.get('likely_to_join', None),
        additional_notes=tour_data.get('additional_notes', None),
        canceled=tour_data.get('canceled', None),
        cancel_reason=tour_data.get('cancel_reason', None),
    )
    return str(id), 200

@app.route('/insert_member', methods=['POST'])
def insert_member():
    member_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_member(
        connection=get_connection(),
        name=member_data.get('name', None),
        age=member_data.get('age', None),
        dob=member_data.get('dob', None),
        email=member_data.get('email', None),
        aep_completion_date=member_data.get('aep_completion_date', None),
        join_date=member_data.get('join_date', None),
        schedule=member_data.get('schedule', None),
        phone=member_data.get('phone', None),
        address=member_data.get('address', None),
        county=member_data.get('county', None),
        gender=member_data.get('gender', None),
        veteran=member_data.get('veteran', None),
        joined=member_data.get('joined', None),
        caregiver_needed=member_data.get('caregiver_needed', None),
        alder_program=member_data.get('alder_program', None),
        notes=member_data.get('notes', None)
    )
    return str(id), 200

@app.route('/insert_membership_enrollment_form', methods=['POST'])
def insert_membership_enrollment_form():
    enrollment_form_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_membership_enrollment_form(
        connection=get_connection(),
        sexual_orientation=enrollment_form_data.get('sexual_orientation', None),
        race=enrollment_form_data.get('race', None),
        income=enrollment_form_data.get('income', None),
        living_status=enrollment_form_data.get('living_status', None),
        grew_up=enrollment_form_data.get('grew_up', None),
        occupations=enrollment_form_data.get('occupations', None),
        prev_speech_therapy=enrollment_form_data.get('prev_speech_therapy', None),
        other_therapy=enrollment_form_data.get('other_therapy', None),
        hearing_loss=enrollment_form_data.get('hearing_loss', None),
        hearing_aid=enrollment_form_data.get('hearing_aid', None),
        aphasia_cause=enrollment_form_data.get('aphasia_cause', None),
        aphasia_onset=enrollment_form_data.get('aphasia_onset', None),
        brain_location=enrollment_form_data.get('brain_location', None),
        medications=enrollment_form_data.get('medications', None),
        filled_by=enrollment_form_data.get('filled_by', None),
        completed_date=enrollment_form_data.get('completed_date', None),
        patient_info=json.dumps(enrollment_form_data.get('patient_info', None))
    )
    return str(id), 200

@app.route('/insert_medical_history_form', methods=['POST'])
def insert_medical_history_form():
    medical_history_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_medical_history_form(
        connection=get_connection(),
        physician_name=medical_history_data.get('physician_name', None),
        specialty=medical_history_data.get('specialty', None),
        physician_address=medical_history_data.get('physician_address', None),
        physician_phone=medical_history_data.get('physician_phone', None),
        aphasia_cause=medical_history_data.get('aphasia_cause', None),
        aphasia_onset=medical_history_data.get('aphasia_onset', None),
        stroke_location=medical_history_data.get('stroke_location', None),
        lesion_location=medical_history_data.get('lesion_location', None),
        primary_diagnosis=medical_history_data.get('primary_diagnosis', None),
        secondary_diagnosis=medical_history_data.get('secondary_diagnosis', None),
        seizure_history=medical_history_data.get('seizure_history', None),
        last_seizure_date=medical_history_data.get('last_seizure_date', None),
        anti_seizure_med=medical_history_data.get('anti_seizure_med', None),
        visual_impairments=medical_history_data.get('visual_impairments', None),
        visual_field_cut=medical_history_data.get('visual_field_cut', None),
        other_visual_impairments=medical_history_data.get('other_visual_impairments', None),
        completion_date=medical_history_data.get('completion_date', None),
        other_medical_conditions=json.dumps(medical_history_data.get('other_medical_conditions', None))
    )
    return str(id), 200

@app.route('/insert_incident_report', methods=['POST'])
def insert_incident_report():
    incident_report_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_incident_report(
        connection=get_connection(),
        incident_date=incident_report_data.get('incident_date', None),
        incident_location=incident_report_data.get('incident_location', None),
        persons_involved=incident_report_data.get('persons_involved', None),
        description=incident_report_data.get('description', None),
        action_taken=incident_report_data.get('action_taken', None),
    )
    return str(id), 200

@app.route('/insert_evaluation', methods=['POST'])
def insert_evaluation():
    evaluation_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_evaluation(
        connection=get_connection(),
        completed=evaluation_data.get('completed', None),
        administerer=evaluation_data.get('administerer', None),
        test_type=evaluation_data.get('test_type', None),
        date_administered=evaluation_data.get('date_administered', None),
    )
    return str(id), 200

@app.route('/insert_transportation_information', methods=['POST'])
def insert_transportation_information():
    transportation_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_transportation_information(
        connection=get_connection(),
        bus_transport=transportation_data.get('bus_transport', None),
        bus_company=transportation_data.get('bus_company', None),
        bus_contact_phone=transportation_data.get('bus_contact_phone', None),
        picked_up=transportation_data.get('picked_up', None),
        pickup_person=transportation_data.get('pickup_person', None),
        relationship_to_member=transportation_data.get('relationship_to_member', None),
        primary_phone=transportation_data.get('primary_phone', None),
        secondary_phone=transportation_data.get('secondary_phone', None),
    )
    return str(id), 200

@app.route('/insert_caregiver', methods=['POST'])
def insert_caregiver():
    caregiver_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_caregiver(
        connection=get_connection(),
        name=caregiver_data.get('name', None),
        phone=caregiver_data.get('phone', None),
        email=caregiver_data.get('email', None),
        relationship=caregiver_data.get('relationship', None),
        date_contacted=caregiver_data.get('date_contacted', None),
        notes=caregiver_data.get('notes', None),
        group_attending=caregiver_data.get('group_attending', None),
        attending=caregiver_data.get('attending', None),
        caregiver_type=caregiver_data.get('caregiver_type', None),
        sex=caregiver_data.get('sex', None),
        race=caregiver_data.get('race', None),
        occupations=caregiver_data.get('occupations', None),
        support_group=caregiver_data.get('support_group', None),
        covid_vaccine_date=caregiver_data.get('covid_vaccine_date', None),
        allergies=caregiver_data.get('allergies', None),
        medications=caregiver_data.get('medications', None),
        participation=caregiver_data.get('participation', None),
        robly=caregiver_data.get('robly', None),
        enrollment_form=caregiver_data.get('enrollment_form', None),
        medical_history=caregiver_data.get('medical_history', None),
        emergency_contact_one=caregiver_data.get('emergency_contact_one', None),
        emergency_contact_two=caregiver_data.get('emergency_contact_two', None),
        transport_info=caregiver_data.get('transport_info', None),
        member_id=caregiver_data.get('member_id', None)
    )
    return str(id), 200

@app.route('/insert_emergency_contact', methods=['POST'])
def insert_emergency_contact():
    emergency_contact_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_emergency_contact(
        connection=get_connection(),
        name=emergency_contact_data.get('name', None),
        relationship=emergency_contact_data.get('relationship', None),
        day_phone=emergency_contact_data.get('day_phone', None),
        evening_phone=emergency_contact_data.get('evening_phone', None),
        cell_phone=emergency_contact_data.get('cell_phone', None),
        email=emergency_contact_data.get('email', None),
        address=emergency_contact_data.get('address', None),
        completion_date=emergency_contact_data.get('completion_date', None),
    )
    return str(id), 200

@app.route('/insert_volunteer', methods=['POST'])
def insert_volunteer():
    volunteer_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_volunteer(
        connection=get_connection(),
        name=volunteer_data.get('name', None),
        phone=volunteer_data.get('phone', None),
        address=volunteer_data.get('address', None),
        email=volunteer_data.get('email', None),
        referral_source=volunteer_data.get('referral_source', None),
        background_check_date=volunteer_data.get('background_check_date', None),
        video_watched_date=volunteer_data.get('video_watched_date', None),
        emergency_contacts=volunteer_data.get('emergency_contacts', None),
        media_release=volunteer_data.get('media_release', None),
        confidentiality=volunteer_data.get('confidentiality', None),
        training_level=volunteer_data.get('training_level', None),
    )
    return str(id), 200

@app.route('/insert_applications', methods=['POST'])
def insert_applications():
    application_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_applications(
        connection=get_connection(),
        birthday=application_data.get('birthday', None),
        occupation=application_data.get('occupation', None),
        is_slp=application_data.get('is_slp', None),
        relevant_experience=application_data.get('relevant_experience', None),
        education=application_data.get('education', None),
        interests_skills_hobbies=application_data.get('interests_skills_hobbies', None),
        languages_spoken=application_data.get('languages_spoken', None),
        will_substitute=application_data.get('will_substitute', None),
        convicted_of_crime=application_data.get('convicted_of_crime', None),
        application_date=application_data.get('application_date', None),
    )
    return str(id), 200

@app.route('/insert_outreach', methods=['POST'])
def insert_outreach():
    outreach_data = json.loads(request.get_json()[0])
    id = insert_functions.insert_outreach(
        connection=get_connection(),
        contacted_date=outreach_data.get('contacted_date', None),
        staff_contacted=outreach_data.get('staff_contacted', None),
        organization=outreach_data.get('organization', None),
        org_type=outreach_data.get('org_type', None),
        outreach_type=outreach_data.get('outreach_type', None),
        target_location=outreach_data.get('target_location', None),
        num_people=outreach_data.get('num_people', None),
        robly=outreach_data.get('robly', None),
        notes=outreach_data.get('notes', None),
    )
    return str(id), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
