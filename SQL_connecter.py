import mysql.connector
import json
from mysql.connector import Error
from datetime import date
from datetime import datetime

def string_to_date(date_string: str) -> datetime.date:
    if date_string:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format. Expected 'yyyy-mm-dd', got {date_string}")
    else: 
        return ''

class get_functions():
    @staticmethod
    def get_contact(connection, id=None, staff_name='', caller_name='', caller_email = '', call_date=None, phone='', referral_type='', tour_scheduled=None, follow_up_date=None):
        cursor = connection.cursor()
        call_date = string_to_date(call_date)
        follow_up_date = string_to_date(follow_up_date)
        # Start building the base query
        query = "SELECT * FROM contact WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments 
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if staff_name:
            query += " AND staff LIKE %s"
            filters.append(f'%{staff_name}%')
        
        if caller_name:
            query += " AND caller_name LIKE %s"
            filters.append(f'%{caller_name}%')
        
        if caller_email:
            query += " AND caller_email LIKE %s"
            filters.append(f'%{caller_email}%')

        if call_date:
            query += " AND call_date = %s"
            filters.append(call_date)
        
        if phone:
            query += " AND phone_number LIKE %s"
            filters.append(f'%{phone}%')
        
        if referral_type:
            query += " AND referral_type LIKE %s"
            filters.append(f'%{referral_type}%')
        
        if tour_scheduled is not None:
            query += " AND tour_scheduled = %s"
            filters.append(tour_scheduled)
        
        if follow_up_date:
            query += " AND follow_up_date = %s"
            filters.append(follow_up_date)
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        # id, staff, caller_name, caller_email, call_date, phone_number, referral_type, additional_notes, tour_scheduled, tour_not_scheduled_reason, follow_up_date
        dict_results = {}
        columns = ["id", "staff", "caller_name", "caller_email", "call_date", "phone_number", "referral_type", "additional_notes", "tour_scheduled", "tour_not_scheduled_reason", "follow_up_date"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results
    
    @staticmethod
    def get_tour(connection,id=None,tour_date=None, attended=None, clinicians='', 
                strategies_used=None, aep_deadline=None, 
                joined_after=None, likely_to_join=None, 
                canceled=None):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM tour WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if tour_date is not None:
            query += " AND tour_date = %s"
            filters.append(tour_date)
        
        if attended is not None:
            query += " AND attended = %s"
            filters.append(attended)
        
        if clinicians:
            query += " AND clinicians LIKE %s"
            filters.append(f'%{clinicians}%')
        
        if strategies_used is not None:
            query += " AND strategies_used = %s"
            filters.append(strategies_used)
        
        if aep_deadline is not None:
            query += " AND aep_deadline = %s"
            filters.append(aep_deadline)
        
        if joined_after is not None:
            query += " AND joined_after = %s"
            filters.append(joined_after)
        
        if likely_to_join is not None:
            query += " AND likely_to_join = %s"
            filters.append(likely_to_join)
        
        if canceled is not None:
            query += " AND canceled = %s"
            filters.append(canceled)
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        results = cursor.fetchall()
        
        # id, tour_date, attended, no_join_reason, clinicians, attendess, interactions, strategies_used, aep_deadline, joined_after, likely_to_join, additional_notes, canceled, cancel_reason
        dict_results = {}
        columns = ["id", "tour_date", "attended", "no_join_reason", "clinicians", "attendess", "interactions", "strategies_used", "aep_deadline", "joined_after", "likely_to_join", "additional_notes", "canceled", "cancel_reason"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results
    
    @staticmethod
    def get_member(connection, id=None,name='', age=None, dob=None, email='', 
                aep_completion_date=None, join_date=None, 
                schedule=None, phone='', address='', 
                county='', gender='', veteran=None, 
                joined=None, caregiver_needed=None, alder_program=''):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM member WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if name:
            query += " AND name LIKE %s"
            filters.append(f'%{name}%')
        
        if age is not None:
            query += " AND age = %s"
            filters.append(age)
        
        if dob is not None:
            query += " AND dob = %s"
            filters.append(dob)
        
        if email:
            query += " AND email LIKE %s"
            filters.append(f'%{email}%')
        
        if aep_completion_date is not None:
            query += " AND aep_completion_date = %s"
            filters.append(aep_completion_date)
        
        if join_date is not None:
            query += " AND join_date = %s"
            filters.append(join_date)
        
        if schedule is not None:
            query += " AND schedule = %s"
            filters.append(schedule)
        
        if phone:
            query += " AND phone LIKE %s"
            filters.append(f'%{phone}%')
        
        if address:
            query += " AND address LIKE %s"
            filters.append(f'%{address}%')
        
        if county:
            query += " AND county LIKE %s"
            filters.append(f'%{county}%')
        
        if gender:
            query += " AND gender = %s"
            filters.append(gender)
        
        if veteran is not None:
            query += " AND veteran = %s"
            filters.append(veteran)
        
        if joined is not None:
            query += " AND joined = %s"
            filters.append(joined)
        
        if caregiver_needed is not None:
            query += " AND caregiver_needed = %s"
            filters.append(caregiver_needed)
        
        if alder_program:
            query += " AND alder_program LIKE %s"
            filters.append(f'%{alder_program}%')
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        results = cursor.fetchall()

        # id, name, age, dob, email, aep_completion_date, join_date, schedule, phone, address, county, gender, veteran, joined, caregiver_needed, adler_program, member_info, enrollment_form, medical_history, emergency_contact_one, emergency_contact_two
        dict_results = {}
        columns = ["id", "name", "age", "dob", "email", "aep_completion_date", "join_date", "schedule", "phone", "address", "county", "gender", "veteran", "joined", "caregiver_needed", "adler_program", "notes", "member_info", "enrollment_form", "medical_history", "emergency_contact_one", "emergency_contact_two", "transport_info"]
        for i in range(len(columns)):
            if columns[i] == "member_info":  # Special handling for member_info
                dict_results[columns[i]] = [
                    json.loads(results[j][i]) if results[j][i] and results[j][i] != "None" else None
                    for j in range(len(results))
                ]
            else:
                dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results
    
    @staticmethod
    def get_membership_enrollment_form(connection, id=None,sexual_orientation='', race='', income=None, 
                                        living_status=None, grew_up='', 
                                        hearing_loss=None, hearing_aid=None, 
                                        aphasia_cause='', aphasia_onset=None, 
                                        brain_location='', filled_by='', 
                                        completed_date=None):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM Membership_Enrollment_Form WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if sexual_orientation:
            query += " AND sexual_orientation LIKE %s"
            filters.append(f'%{sexual_orientation}%')
        
        if race:
            query += " AND race LIKE %s"
            filters.append(f'%{race}%')
        
        if income is not None:
            query += " AND income = %s"
            filters.append(income)
        
        if living_status is not None:
            query += " AND living_status = %s"
            filters.append(living_status)
        
        if grew_up:
            query += " AND grew_up LIKE %s"
            filters.append(f'%{grew_up}%')
        
        if hearing_loss is not None:
            query += " AND hearing_loss = %s"
            filters.append(hearing_loss)
        
        if hearing_aid is not None:
            query += " AND hearing_aid = %s"
            filters.append(hearing_aid)
        
        if aphasia_cause:
            query += " AND aphasia_cause LIKE %s"
            filters.append(f'%{aphasia_cause}%')
        
        if aphasia_onset is not None:
            query += " AND aphasia_onset = %s"
            filters.append(aphasia_onset)
        
        if brain_location:
            query += " AND brain_location LIKE %s"
            filters.append(f'%{brain_location}%')
        
        if filled_by:
            query += " AND filled_by LIKE %s"
            filters.append(f'%{filled_by}%')
        
        if completed_date is not None:
            query += " AND completed_date = %s"
            filters.append(completed_date)
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        
        # id, sexual_orientation, race, income, living_status, grew_up, occupations, prev_speech_therapy, other_therapy, hearing_loss, hearing_aid, aphasia_cause, aphasia_onset, brain_location, medications, filled_by, completed_date, patient_info
        dict_results = {}
        columns = ["id", "sexual_orientation", "race", "income", "living_status", "grew_up", "occupations", "prev_speech_therapy", "other_therapy", "hearing_loss", "hearing_aid", "aphasia_cause", "aphasia_onset", "brain_location", "medications", "filled_by", "completed_date", "patient_info"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results
    
    @staticmethod
    def get_medical_history_form(connection, id=None, physician_name='', specialty='', 
                                physician_address='', physician_phone='', 
                                aphasia_cause='', aphasia_onset=None, 
                                stroke_location='', lesion_location='', 
                                primary_diagnosis='', secondary_diagnosis='', 
                                seizure_history=None, last_seizure_date=None, 
                                anti_seizure_med=None,
                                visual_impairments='',
                                visual_field_cut=None,
                                other_visual_impairments='',
                                completion_date=None):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM Medical_History_Form WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if physician_name:
            query += " AND physician_name LIKE %s"
            filters.append(f'%{physician_name}%')
        
        if specialty:
            query += " AND specialty LIKE %s"
            filters.append(f'%{specialty}%')
        
        if physician_address:
            query += " AND physician_address LIKE %s"
            filters.append(f'%{physician_address}%')
        
        if physician_phone:
            query += " AND physician_phone LIKE %s"
            filters.append(f'%{physician_phone}%')
        
        if aphasia_cause:
            query += " AND aphasia_cause LIKE %s"
            filters.append(f'%{aphasia_cause}%')
        
        if aphasia_onset is not None:
            query += " AND aphasia_onset = %s"
            filters.append(aphasia_onset)
        
        if stroke_location:
            query += " AND stroke_location = %s"
            filters.append(stroke_location)
        
        if lesion_location:
            query += " AND lesion_location LIKE %s"
            filters.append(f'%{lesion_location}%')
        
        if primary_diagnosis:
            query += " AND primary_diagnosis LIKE %s"
            filters.append(f'%{primary_diagnosis}%')
        
        if secondary_diagnosis:
            query += " AND secondary_diagnosis LIKE %s"
            filters.append(f'%{secondary_diagnosis}%')
        
        if seizure_history is not None:
            query += " AND seizure_history = %s"
            filters.append(seizure_history)
        
        if last_seizure_date is not None:
            query += " AND last_seizure_date = %s"
            filters.append(last_seizure_date)
        
        if anti_seizure_med is not None:
            query += " AND anti_seizure_med = %s"
            filters.append(anti_seizure_med)

        if visual_impairments:
            query += " AND visual_impairments LIKE %s"
            filters.append(f'%{visual_impairments}%')

        if visual_field_cut is not None:
            query += " AND visual_field_cut = %s"
            filters.append(visual_field_cut)
        
        if other_visual_impairments:
            query += " AND other_visual_impairments LIKE %s"
            filters.append(f'%{other_visual_impairments}%')
        
        if completion_date is not None:
            query += " AND completion_date = %s"
            filters.append(completion_date)
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        
        # physician_name
        # specialty
        # physician_address
        # physician_phone
        # aphasia_cause
        # aphasia_onset
        # stroke_location
        # lesion_location
        # primary_diagnosis
        # secondary_diagnosis
        # seizure_history
        # last_seizure_date
        # anti_seizure_med
        # visual_impairments
        # visual_field_cut
        # other_visual_impairments
        # completion_date
        dict_results = {}
        columns = ["id", "physicion_name", "specialty", "physician_address", "physician_phone", "aphasia_cause", "aphasia_onset", "stroke_location", "lesion_location", "primary_diagnosis", "secondary_diagnosis", "seizure_history", "last_seizure_date", "anti_seizure_med", "visual_impairments", "visual_field_cut", "other_visual_impairments", "completion_date", "other_medical_conditions"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results
    
    @staticmethod
    def get_incident_report(connection, id=None, incident_date=None, incident_location=''):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM Incident_Report WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if incident_date is not None:
            query += " AND incident_date = %s"
            filters.append(incident_date)
        
        if incident_location:
            query += " AND incident_location LIKE %s"
            filters.append(f'%{incident_location}%')
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        
        # incident_date, incident_location, persons_involved, description, action_taken
        dict_results = {}
        columns = ["id","incident_date", "incident_location", "persons_involved", "description", "action_taken"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results
    
    @staticmethod
    def get_evaluation(connection, id=None, completed=None, administerer='', date_administered=None):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM Evaluation WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if completed is not None:
            query += " AND completed = %s"
            filters.append(completed)
        
        if administerer:
            query += " AND administerer LIKE %s"
            filters.append(f'%{administerer}%')
        
        if date_administered is not None:
            query += " AND date_administered = %s"
            filters.append(date_administered)
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        
        dict_results = {}
        columns = ["id","completed", "administerer", "test_type", "date_administered"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results

    
    @staticmethod
    def get_transportation_information(connection, id=None, bus_transport=None, bus_company='', 
                                        bus_contact_phone='', picked_up=None, 
                                        pickup_person='', relationship_to_member='', 
                                        primary_phone='', secondary_phone=''):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM Transportation_Information WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if bus_transport is not None:
            query += " AND bus_transport = %s"
            filters.append(bus_transport)
        
        if bus_company:
            query += " AND bus_company LIKE %s"
            filters.append(f'%{bus_company}%')
        
        if bus_contact_phone:
            query += " AND bus_contact_phone LIKE %s"
            filters.append(f'%{bus_contact_phone}%')
        
        if picked_up is not None:
            query += " AND picked_up = %s"
            filters.append(picked_up)
        
        if pickup_person:
            query += " AND pickup_person LIKE %s"
            filters.append(f'%{pickup_person}%')
        
        if relationship_to_member:
            query += " AND relationship_to_member LIKE %s"
            filters.append(f'%{relationship_to_member}%')
        
        if primary_phone:
            query += " AND primary_phone LIKE %s"
            filters.append(f'%{primary_phone}%')
        
        if secondary_phone:
            query += " AND secondary_phone LIKE %s"
            filters.append(f'%{secondary_phone}%')
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        
        dict_results = {}
        columns = ["id","bus_transport", "bus_company", "bus_contact_phone", "picked_up", "pickup_person", "relationship_to_member", "primary_phone", "secondary_phone"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results

    @staticmethod
    def get_caregiver(
        connection, id=None, name='', phone='', email='', relationship='', date_contacted=None,
        group_attending='', attending=None, caregiver_type='', sex='', race='', occupations='',
        support_group=None, allergies='', medications='', participation='', robly=None,
        enrollment_form=None, medical_history=None, emergency_contact_one=None,
        emergency_contact_two=None, transport_info=None, member_id=None
    ):
        cursor = connection.cursor()

        # Start building the base query
        query = "SELECT * FROM Caregiver WHERE 1=1"
        filters = []

        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)
        if name:
            query += " AND name LIKE %s"
            filters.append(f'%{name}%')
        if phone:
            query += " AND phone LIKE %s"
            filters.append(f'%{phone}%')
        if email:
            query += " AND email LIKE %s"
            filters.append(f'%{email}%')
        if relationship:
            query += " AND relationship LIKE %s"
            filters.append(f'%{relationship}%')
        if date_contacted is not None:
            query += " AND date_contacted = %s"
            filters.append(date_contacted)
        if group_attending:
            query += " AND group_attending LIKE %s"
            filters.append(f'%{group_attending}%')
        if attending is not None:
            query += " AND attending = %s"
            filters.append(attending)
        if caregiver_type:
            query += " AND caregiver_type LIKE %s"
            filters.append(f'%{caregiver_type}%')
        if sex:
            query += " AND sex = %s"
            filters.append(sex)
        if race:
            query += " AND race LIKE %s"
            filters.append(f'%{race}%')
        if occupations:
            query += " AND occupations LIKE %s"
            filters.append(f'%{occupations}%')
        if support_group is not None:
            query += " AND support_group = %s"
            filters.append(support_group)
        if allergies:
            query += " AND allergies LIKE %s"
            filters.append(f'%{allergies}%')
        if medications:
            query += " AND medications LIKE %s"
            filters.append(f'%{medications}%')
        if participation:
            query += " AND participation LIKE %s"
            filters.append(f'%{participation}%')
        if robly is not None:
            query += " AND robly = %s"
            filters.append(robly)
        if enrollment_form is not None:
            query += " AND enrollment_form = %s"
            filters.append(enrollment_form)
        if medical_history is not None:
            query += " AND medical_history = %s"
            filters.append(medical_history)
        if emergency_contact_one is not None:
            query += " AND emergency_contact_one = %s"
            filters.append(emergency_contact_one)
        if emergency_contact_two is not None:
            query += " AND emergency_contact_two = %s"
            filters.append(emergency_contact_two)
        if transport_info is not None:
            query += " AND transport_info = %s"
            filters.append(transport_info)
        if member_id is not None:
            query += " AND member_id = %s"
            filters.append(member_id)

        # Execute the query with filters
        cursor.execute(query, tuple(filters))

        # Fetch all results
        results = cursor.fetchall()

        # Define the columns
        columns = ['id', 'name', 'phone', 'email', 'relationship', 'date_contacted', 'notes', 'group_attending', 'attending', 'caregiver_type', 'sex', 'race', 'occupations', 'support_group', 'covid_vaccine_date', 'allergies', 'medications', 'participation', 'robly', 'enrollment_form', 'medical_history', 'emergency_contact_one', 'emergency_contact_two', 'transport_info', 'member_id']

        # Map results to a dictionary
        dict_results = {}
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]

        if connection:
            connection.close()
        return dict_results

    @staticmethod
    def get_emergency_contact(connection, id=None, name='', relationship='', day_phone='', 
                            evening_phone='', cell_phone='', 
                            address='', completion_date=None):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM Emergency_Contact WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if name:
            query += " AND name LIKE %s"
            filters.append(f'%{name}%')
        
        if relationship:
            query += " AND relationship LIKE %s"
            filters.append(f'%{relationship}%')
        
        if day_phone:
            query += " AND day_phone = %s"
            filters.append(f'{day_phone}')
        
        if evening_phone:
            query += " AND evening_phone = %s"
            filters.append(f'{evening_phone}')
        
        if cell_phone:
            query += " AND cell_phone = %s"
            filters.append(f'{cell_phone}')
        
        if address:
            query += " AND address LIKE %s"
            filters.append(f'%{address}%')
        
        if completion_date is not None:
            query += " AND completion_date = %s"
            filters.append(completion_date)
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        
        dict_results = {}
        columns = ["id", "name", "relationship", "day_phone", "evening_phone", "cell_phone", "email", "address", "completion_date"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results

    
    @staticmethod
    def get_volunteer(connection, id=None, name='', phone='', address='', email='', 
                    background_check_date=None, video_watched_date=None, 
                    media_release=None, confidentiality=None, 
                    training_level=None):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM Volunteer WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if name:
            query += " AND name LIKE %s"
            filters.append(f'%{name}%')
        
        if phone:
            query += " AND phone = %s"
            filters.append(f'{phone}')
        
        if address:
            query += " AND address LIKE %s"
            filters.append(f'%{address}%')
        
        if email:
            query += " AND email LIKE %s"
            filters.append(f'%{email}%')
        
        if background_check_date is not None:
            query += " AND background_check_date = %s"
            filters.append(background_check_date)
        
        if video_watched_date is not None:
            query += " AND video_watched_date = %s"
            filters.append(video_watched_date)
        
        if media_release is not None:
            query += " AND media_release = %s"
            filters.append(media_release)
        
        if confidentiality is not None:
            query += " AND confidentiality = %s"
            filters.append(confidentiality)
        
        if training_level is not None:
            query += " AND training_level = %s"
            filters.append(training_level)
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        
        dict_results = {}
        columns = ["id", "name", "phone", "address", "email", "referral_source", "background_check_date", "video_watched_date", "emergency_contacts", "media_release", "confidentiality", "training_level"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()
        return dict_results

    
    @staticmethod
    def get_applications(connection, id=None, birthday=None, occupation='', is_slp=None, 
                        languages_spoken='', will_substitute=None, 
                        convicted_of_crime=None, application_date=None):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM Applications WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)

        if birthday is not None:
            query += " AND birthday = %s"
            filters.append(birthday)
        
        if occupation:
            query += " AND occupation LIKE %s"
            filters.append(f'%{occupation}%')
        
        if is_slp is not None:
            query += " AND is_slp = %s"
            filters.append(is_slp)
        
        if languages_spoken:
            query += " AND languages_spoken LIKE %s"
            filters.append(f'%{languages_spoken}%')
        
        if will_substitute is not None:
            query += " AND will_substitute = %s"
            filters.append(will_substitute)
        
        if convicted_of_crime is not None:
            query += " AND convicted_of_crime = %s"
            filters.append(convicted_of_crime)
        
        if application_date is not None:
            query += " AND application_date = %s"
            filters.append(application_date)
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        
        dict_results = {}
        columns = ["id", "birthday", "occupation", "is_slp", "relevant_experience", "education", "interests_skills_hobbies", "languages_spoken", "will_substitute", "convicted_of_crime", "application_date"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()    
        return dict_results

    
    @staticmethod
    def get_outreach(connection, id=None, contacted_date=None, staff_contacted='', 
                    organization='', org_type='', outreach_type='', 
                    target_location='', num_people=None, robly=None):
        cursor = connection.cursor()
        
        # Start building the base query
        query = "SELECT * FROM Outreach WHERE 1=1"
        filters = []
        
        # Append conditions based on provided arguments
        if id is not None:
            query += " AND id = %s"
            filters.append(id)
            
        if contacted_date is not None:
            query += " AND contacted_date = %s"
            filters.append(contacted_date)
        
        if staff_contacted:
            query += " AND staff_contacted LIKE %s"
            filters.append(f'%{staff_contacted}%')
        
        if organization:
            query += " AND organization LIKE %s"
            filters.append(f'%{organization}%')
        
        if org_type:
            query += " AND org_type LIKE %s"
            filters.append(f'%{org_type}%')
        
        if outreach_type:
            query += " AND outreach_type LIKE %s"
            filters.append(f'%{outreach_type}%')
        
        if target_location:
            query += " AND target_location LIKE %s"
            filters.append(f'%{target_location}%')
        
        if num_people is not None:
            query += " AND num_people = %s"
            filters.append(num_people)
        
        if robly is not None:
            query += " AND robly = %s"
            filters.append(robly)
        
        # Execute the query with filters
        cursor.execute(query, tuple(filters))
        
        # Fetch all results
        results = cursor.fetchall()
        
        dict_results = {}
        columns = ["id", "contacted_date", "staff_contacted", "organization", "org_type", "outreach_type", "target_location", "num_people", "robly", "notes"]
        for i in range(len(columns)):
            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
        if connection:
            connection.close()    
        return dict_results

class update_functions():
    @staticmethod
    def update_contact(
        connection, id, staff=None, caller_name=None, caller_email=None, call_date=None, 
        phone_number=None, referral_type=None, additional_notes=None, 
        tour_scheduled=None, tour_not_scheduled_reason=None, follow_up_date=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Contact SET "
        update_values = []
        
        # Dynamically append fields to update query and values to update_values
        if staff:
            update_query += "staff = %s, "
            update_values.append(staff)
        if caller_name:
            update_query += "caller_name = %s, "
            update_values.append(caller_name)
        if caller_email:
            update_query += "caller_email = %s, "
            update_values.append(caller_email)
        if call_date:
            update_query += "call_date = %s, "
            update_values.append(call_date)
        if phone_number:
            update_query += "phone_number = %s, "
            update_values.append(phone_number)
        if referral_type:
            update_query += "referral_type = %s, "
            update_values.append(referral_type)
        if additional_notes:
            update_query += "additional_notes = %s, "
            update_values.append(additional_notes)
        if tour_scheduled is not None:
            update_query += "tour_scheduled = %s, "
            update_values.append(tour_scheduled)
        if tour_not_scheduled_reason:
            update_query += "tour_not_scheduled_reason = %s, "
            update_values.append(tour_not_scheduled_reason)
        if follow_up_date:
            update_query += "follow_up_date = %s, "
            update_values.append(follow_up_date)

        # Remove the last comma and space from the query
        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_tour(
            connection, id, tour_date=None, attended=None, no_join_reason=None, clinicians=None, 
            attendees=None, interactions=None, strategies_used=None, aep_deadline=None, 
            joined_after=None, likely_to_join=None, additional_notes=None, canceled=None, 
            cancel_reason=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Tour SET "
        update_values = []

        # Dynamically add conditions to the query
        if tour_date:
            update_query += "tour_date = %s, "
            update_values.append(tour_date)
        if attended is not None:
            update_query += "attended = %s, "
            update_values.append(attended)
        if no_join_reason:
            update_query += "no_join_reason = %s, "
            update_values.append(no_join_reason)
        if clinicians:
            update_query += "clinicians = %s, "
            update_values.append(clinicians)
        if attendees:
            update_query += "attendees = %s, "
            update_values.append(attendees)
        if interactions:
            update_query += "interactions = %s, "
            update_values.append(interactions)
        if strategies_used is not None:
            update_query += "strategies_used = %s, "
            update_values.append(strategies_used)
        if aep_deadline:
            update_query += "aep_deadline = %s, "
            update_values.append(aep_deadline)
        if joined_after is not None:
            update_query += "joined_after = %s, "
            update_values.append(joined_after)
        if likely_to_join is not None:
            update_query += "likely_to_join = %s, "
            update_values.append(likely_to_join)
        if additional_notes:
            update_query += "additional_notes = %s, "
            update_values.append(additional_notes)
        if canceled is not None:
            update_query += "canceled = %s, "
            update_values.append(canceled)
        if cancel_reason:
            update_query += "cancel_reason = %s, "
            update_values.append(cancel_reason)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_member(
            connection, id, name=None, age=None, dob=None, email=None, aep_completion_date=None, 
            join_date=None, schedule=None, phone=None, address=None, county=None, 
            gender=None, veteran=None, joined=None, caregiver_needed=None, medical_history = None,
            alder_program=None, emergency_contact_one = None, emergency_contact_two = None, enrollment_form = None, notes = None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Member SET "
        update_values = []

        if name:
            update_query += "name = %s, "
            update_values.append(name)
        if age is not None:
            update_query += "age = %s, "
            update_values.append(age)
        if dob:
            update_query += "dob = %s, "
            update_values.append(dob)
        if email:
            update_query += "email = %s, "
            update_values.append(email)
        if aep_completion_date:
            update_query += "aep_completion_date = %s, "
            update_values.append(aep_completion_date)
        if join_date:
            update_query += "join_date = %s, "
            update_values.append(join_date)
        if schedule is not None:
            update_query += "schedule = %s, "
            update_values.append(schedule)
        if phone:
            update_query += "phone = %s, "
            update_values.append(phone)
        if address:
            update_query += "address = %s, "
            update_values.append(address)
        if county:
            update_query += "county = %s, "
            update_values.append(county)
        if gender:
            update_query += "gender = %s, "
            update_values.append(gender)
        if veteran is not None:
            update_query += "veteran = %s, "
            update_values.append(veteran)
        if joined is not None:
            update_query += "joined = %s, "
            update_values.append(joined)
        if caregiver_needed is not None:
            update_query += "caregiver_needed = %s, "
            update_values.append(caregiver_needed)
        if alder_program:
            update_query += "alder_program = %s, "
            update_values.append(alder_program)
        if medical_history:
            update_query += "medical_history = %s, "
            update_values.append(medical_history)
        if emergency_contact_one:
            update_query += "emergency_contact_one = %s, "
            update_values.append(emergency_contact_one)
        if emergency_contact_two:
            update_query += "emergency_contact_two = %s, "
            update_values.append(emergency_contact_two)
        if enrollment_form:
            update_query += "enrollment_form = %s, "
            update_values.append(enrollment_form)
        if notes:
            update_query += "notes = %s, "
            update_values.append(notes)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_membership_enrollment_form(
            connection, id, sexual_orientation=None, race=None, income=None, 
            living_status=None, grew_up=None, occupations=None, 
            prev_speech_therapy=None, other_therapy=None, 
            hearing_loss=None, hearing_aid=None, aphasia_cause=None, 
            aphasia_onset=None, brain_location=None, allergies=None, 
            medications=None, filled_by=None, completed_date=None, patient_info=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Membership_Enrollment_Form SET "
        update_values = []

        if sexual_orientation:
            update_query += "sexual_orientation = %s, "
            update_values.append(sexual_orientation)
        if race:
            update_query += "race = %s, "
            update_values.append(race)
        if income is not None:
            update_query += "income = %s, "
            update_values.append(income)
        if living_status is not None:
            update_query += "living_status = %s, "
            update_values.append(living_status)
        if grew_up:
            update_query += "grew_up = %s, "
            update_values.append(grew_up)
        if occupations:
            update_query += "occupations = %s, "
            update_values.append(occupations)
        if prev_speech_therapy:
            update_query += "prev_speech_therapy = %s, "
            update_values.append(prev_speech_therapy)
        if other_therapy:
            update_query += "other_therapy = %s, "
            update_values.append(other_therapy)
        if hearing_loss is not None:
            update_query += "hearing_loss = %s, "
            update_values.append(hearing_loss)
        if hearing_aid is not None:
            update_query += "hearing_aid = %s, "
            update_values.append(hearing_aid)
        if aphasia_cause:
            update_query += "aphasia_cause = %s, "
            update_values.append(aphasia_cause)
        if aphasia_onset:
            update_query += "aphasia_onset = %s, "
            update_values.append(aphasia_onset)
        if brain_location:
            update_query += "brain_location = %s, "
            update_values.append(brain_location)
        if allergies:
            update_query += "allergies = %s, "
            update_values.append(allergies)
        if medications:
            update_query += "medications = %s, "
            update_values.append(medications)
        if filled_by:
            update_query += "filled_by = %s, "
            update_values.append(filled_by)
        if completed_date:
            update_query += "completed_date = %s, "
            update_values.append(completed_date)
        if patient_info:
            update_query += "patient_info = %s, "
            update_values.append(patient_info)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_medical_history_form(
            connection, id, physician_name=None, specialty=None, physician_address=None, 
            physician_phone=None, aphasia_cause=None, aphasia_onset=None, 
            stroke_location=None, lesion_location=None, primary_diagnosis=None, 
            secondary_diagnosis=None, seizure_history=None, last_seizure_date=None, 
            anti_seizure_med=None, visual_impairments=None, visual_field_cut=None, 
            other_visual_impairments=None, completion_date=None, other_medical_conditions=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Medical_History_Form SET "
        update_values = []

        if physician_name:
            update_query += "physician_name = %s, "
            update_values.append(physician_name)
        if specialty:
            update_query += "specialty = %s, "
            update_values.append(specialty)
        if physician_address:
            update_query += "physician_address = %s, "
            update_values.append(physician_address)
        if physician_phone:
            update_query += "physician_phone = %s, "
            update_values.append(physician_phone)
        if aphasia_cause:
            update_query += "aphasia_cause = %s, "
            update_values.append(aphasia_cause)
        if aphasia_onset:
            update_query += "aphasia_onset = %s, "
            update_values.append(aphasia_onset)
        if stroke_location:
            update_query += "stroke_location = %s, "
            update_values.append(stroke_location)
        if lesion_location:
            update_query += "lesion_location = %s, "
            update_values.append(lesion_location)
        if primary_diagnosis:
            update_query += "primary_diagnosis = %s, "
            update_values.append(primary_diagnosis)
        if secondary_diagnosis:
            update_query += "secondary_diagnosis = %s, "
            update_values.append(secondary_diagnosis)
        if seizure_history is not None:
            update_query += "seizure_history = %s, "
            update_values.append(seizure_history)
        if last_seizure_date:
            update_query += "last_seizure_date = %s, "
            update_values.append(last_seizure_date)
        if anti_seizure_med is not None:
            update_query += "anti_seizure_med = %s, "
            update_values.append(anti_seizure_med)
        if visual_impairments:
            update_query += "visual_impairments = %s, "
            update_values.append(visual_impairments)
        if visual_field_cut is not None:
            update_query += "visual_field_cut = %s, "
            update_values.append(visual_field_cut)
        if other_visual_impairments:
            update_query += "other_visual_impairments = %s, "
            update_values.append(other_visual_impairments)
        if completion_date:
            update_query += "completion_date = %s, "
            update_values.append(completion_date)
        if other_medical_conditions:
            update_query += "other_conditions = %s, "
            update_values.append(other_medical_conditions)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_incient_report(
            connection, id, incident_date=None, incident_location=None, persons_involved=None, 
            description=None, action_taken=None 
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Incident_Report SET "
        update_values = []

        if incident_date:
            update_query += "incident_date = %s, "
            update_values.append(incident_date)
        if incident_location:
            update_query += "incident_location = %s, "
            update_values.append(incident_location)
        if persons_involved:
            update_query += "persons_involved = %s, "
            update_values.append(persons_involved)
        if description:
            update_query += "description = %s, "
            update_values.append(description)
        if action_taken:
            update_query += "action_taken = %s, "
            update_values.append(action_taken)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_evaluation(
        connection, id, completed=None, administerer=None, test_type=None, date_administered=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Evaluation SET "
        update_values = []

        if completed is not None:
            update_query += "completed = %s, "
            update_values.append(completed)
        if administerer:
            update_query += "administerer = %s, "
            update_values.append(administerer)
        if test_type:
            update_query += "test_type = %s, "
            update_values.append(test_type)
        if date_administered:
            update_query += "date_administered = %s, "
            update_values.append(date_administered)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_transportation_information(
            connection, id, bus_transport=None, bus_company=None, bus_contact_phone=None,
            picked_up=None, pickup_person=None, relationship_to_member=None, 
            primary_phone=None, secondary_phone=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Transportation_Information SET "
        update_values = []
        if bus_transport is not None:
            update_query += "bus_transport = %s, "
            update_values.append(bus_transport)
        if bus_company:
            update_query += "bus_company = %s, "
            update_values.append(bus_company)
        if bus_contact_phone:
            update_query += "bus_contact_phone = %s, "
            update_values.append(bus_contact_phone)
        if picked_up is not None:
            update_query += "picked_up = %s, "
            update_values.append(picked_up)
        if pickup_person:
            update_query += "pickup_person = %s, "
            update_values.append(pickup_person)
        if relationship_to_member:
            update_query += "relationship_to_member = %s, "
            update_values.append(relationship_to_member)
        if primary_phone:
            update_query += "primary_phone = %s, "
            update_values.append(primary_phone)
        if secondary_phone:
            update_query += "secondary_phone = %s, "
            update_values.append(secondary_phone)
        

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_caregiver(
        connection, id, name=None, phone=None, email=None, relationship=None, date_contacted=None,
        notes=None, group_attending=None, attending=None, caregiver_type=None, sex=None, race=None,
        occupations=None, support_group=None, covid_vaccine_date=None, allergies=None, medications=None,
        participation=None, robly=None, enrollment_form=None, medical_history=None,
        emergency_contact_one=None, emergency_contact_two=None, transport_info=None, member_id=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Caregiver SET "
        update_values = []

        if name:
            update_query += "name = %s, "
            update_values.append(name)
        if phone:
            update_query += "phone = %s, "
            update_values.append(phone)
        if email:
            update_query += "email = %s, "
            update_values.append(email)
        if relationship:
            update_query += "relationship = %s, "
            update_values.append(relationship)
        if date_contacted:
            update_query += "date_contacted = %s, "
            update_values.append(date_contacted)
        if notes:
            update_query += "notes = %s, "
            update_values.append(notes)
        if group_attending:
            update_query += "group_attending = %s, "
            update_values.append(group_attending)
        if attending is not None:
            update_query += "attending = %s, "
            update_values.append(attending)
        if caregiver_type:
            update_query += "caregiver_type = %s, "
            update_values.append(caregiver_type)
        if sex:
            update_query += "sex = %s, "
            update_values.append(sex)
        if race:
            update_query += "race = %s, "
            update_values.append(race)
        if occupations:
            update_query += "occupations = %s, "
            update_values.append(occupations)
        if support_group is not None:
            update_query += "support_group = %s, "
            update_values.append(support_group)
        if covid_vaccine_date:
            update_query += "covid_vaccine_date = %s, "
            update_values.append(covid_vaccine_date)
        if allergies:
            update_query += "allergies = %s, "
            update_values.append(allergies)
        if medications:
            update_query += "medications = %s, "
            update_values.append(medications)
        if participation:
            update_query += "participation = %s, "
            update_values.append(participation)
        if robly is not None:
            update_query += "robly = %s, "
            update_values.append(robly)
        if enrollment_form is not None:
            update_query += "enrollment_form = %s, "
            update_values.append(enrollment_form)
        if medical_history is not None:
            update_query += "medical_history = %s, "
            update_values.append(medical_history)
        if emergency_contact_one is not None:
            update_query += "emergency_contact_one = %s, "
            update_values.append(emergency_contact_one)
        if emergency_contact_two is not None:
            update_query += "emergency_contact_two = %s, "
            update_values.append(emergency_contact_two)
        if transport_info is not None:
            update_query += "transport_info = %s, "
            update_values.append(transport_info)
        if member_id is not None:
            update_query += "member_id = %s, "
            update_values.append(member_id)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caregiver by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_emergency_contact(
            connection, id, name=None, relationship=None, day_phone=None, evening_phone=None, 
            cell_phone=None, email=None, address=None, completion_date=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Emergency_Contact SET "
        update_values = []

        if name:
            update_query += "name = %s, "
            update_values.append(name)
        if relationship:
            update_query += "relationship = %s, "
            update_values.append(relationship)
        if day_phone:
            update_query += "day_phone = %s, "
            update_values.append(day_phone)
        if evening_phone:
            update_query += "evening_phone = %s, "
            update_values.append(evening_phone)
        if cell_phone:
            update_query += "cell_phone = %s, "
            update_values.append(cell_phone)
        if email:
            update_query += "email = %s, "
            update_values.append(email)
        if address:
            update_query += "address = %s, "
            update_values.append(address)
        if completion_date:
            update_query += "completion_date = %s, "
            update_values.append(completion_date)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_volunteer(
        connection, id, name=None, phone=None, address=None, email=None, referral_source=None, 
        background_check_date=None, video_watched_date=None, emergency_contacts=None, 
        media_release=None, confidentiality=None, training_level=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Volunteer SET "
        update_values = []

        if name:
            update_query += "name = %s, "
            update_values.append(name)
        if phone:
            update_query += "phone = %s, "
            update_values.append(phone)
        if address:
            update_query += "address = %s, "
            update_values.append(address)
        if email:
            update_query += "email = %s, "
            update_values.append(email)
        if referral_source:
            update_query += "referral_source = %s, "
            update_values.append(referral_source)
        if background_check_date:
            update_query += "background_check_date = %s, "
            update_values.append(background_check_date)
        if video_watched_date:
            update_query += "video_watched_date = %s, "
            update_values.append(video_watched_date)
        if emergency_contacts:
            update_query += "emergency_contacts = %s, "
            update_values.append(emergency_contacts)
        if media_release is not None:
            update_query += "media_release = %s, "
            update_values.append(media_release)
        if confidentiality is not None:
            update_query += "confidentiality = %s, "
            update_values.append(confidentiality)
        if training_level is not None:
            update_query += "training_level = %s, "
            update_values.append(training_level)        

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id


    @staticmethod
    def update_applications(
            connection, id, birthday=None, occupation=None, is_slp=None, relevant_experience=None, 
            education=None, interests_skills_hobbies=None, languages_spoken=None, 
            will_substitute=None, convicted_of_crime=None, application_date=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Applications SET "
        update_values = []

        if birthday:
            update_query += "birthday = %s, "
            update_values.append(birthday)
        if occupation:
            update_query += "occupation = %s, "
            update_values.append(occupation)
        if is_slp is not None:
            update_query += "is_slp = %s, "
            update_values.append(is_slp)
        if relevant_experience:
            update_query += "relevant_experience = %s, "
            update_values.append(relevant_experience)
        if education:
            update_query += "education = %s, "
            update_values.append(education)
        if interests_skills_hobbies:
            update_query += "interests_skills_hobbies = %s, "
            update_values.append(interests_skills_hobbies)
        if languages_spoken:
            update_query += "languages_spoken = %s, "
            update_values.append(languages_spoken)
        if will_substitute is not None:
            update_query += "will_substitute = %s, "
            update_values.append(will_substitute)
        if convicted_of_crime is not None:
            update_query += "convicted_of_crime = %s, "
            update_values.append(convicted_of_crime)
        if application_date:
            update_query += "application_date = %s, "
            update_values.append(application_date)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

    @staticmethod
    def update_outreach(
            connection, id, contacted_date=None, staff_contacted=None, organization=None, org_type=None, 
            outreach_type=None, target_location=None, num_people=None, robly=None, notes=None
    ):
        cursor = connection.cursor()
        update_query = "UPDATE Outreach SET "
        update_values = []

        if contacted_date:
            update_query += "contacted_date = %s, "
            update_values.append(contacted_date)
        if staff_contacted:
            update_query += "staff_contacted = %s, "
            update_values.append(staff_contacted)
        if organization:
            update_query += "organization = %s, "
            update_values.append(organization)
        if org_type:
            update_query += "org_type = %s, "
            update_values.append(org_type)
        if outreach_type:
            update_query += "outreach_type = %s, "
            update_values.append(outreach_type)
        if target_location:
            update_query += "target_location = %s, "
            update_values.append(target_location)
        if num_people is not None:
            update_query += "num_people = %s, "
            update_values.append(num_people)
        if robly is not None:
            update_query += "robly = %s, "
            update_values.append(robly)
        if notes:
            update_query += "notes = %s, "
            update_values.append(notes)

        update_query = update_query.rstrip(", ")

        # Add the condition to update the specific caller by id
        update_query += " WHERE id = %s"
        update_values.append(id)

        # Execute the query
        cursor.execute(update_query, tuple(update_values))

        # Commit the transaction
        connection.commit()
        if connection:
            connection.close()
        return id

class insert_functions():
    @staticmethod
    def insert_contact(
        connection, staff, caller_name, caller_email, call_date, phone_number,
        referral_type, additional_notes, tour_scheduled, 
        tour_not_scheduled_reason, follow_up_date
    ):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Contact (
            staff, caller_name, caller_email, call_date, phone_number, 
            referral_type, additional_notes, tour_scheduled, 
            tour_not_scheduled_reason, follow_up_date
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        data = (
            staff, caller_name, caller_email, call_date, phone_number, 
            referral_type, additional_notes, tour_scheduled, 
            tour_not_scheduled_reason, follow_up_date
        )
        
        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_tour(
        connection, tour_date, attended, no_join_reason, clinicians, attendees, 
        interactions, strategies_used, aep_deadline, joined_after, 
        likely_to_join, additional_notes, canceled, cancel_reason
    ):
        cursor = connection.cursor()
        
        cursor.execute("""
        INSERT INTO Tour (
            tour_date, attended, no_join_reason, clinicians, attendees, 
            interactions, strategies_used, aep_deadline, joined_after, 
            likely_to_join, additional_notes, canceled, cancel_reason
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            tour_date, attended, no_join_reason, clinicians, attendees, 
            interactions, strategies_used, aep_deadline, joined_after, 
            likely_to_join, additional_notes, canceled, cancel_reason
        ))

        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_member(connection, name, age, dob, email, aep_completion_date, join_date, schedule, 
                  phone, address, county, gender, veteran, joined, caregiver_needed, 
                  alder_program, notes):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Member (
            name, age, dob, email, aep_completion_date, join_date, schedule, 
            phone, address, county, gender, veteran, joined, caregiver_needed, 
            alder_program, member_info, notes
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            name, age, dob, email, aep_completion_date, join_date, schedule, 
            phone, address, county, gender, veteran, joined, caregiver_needed, 
            alder_program, notes
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_membership_enrollment_form(connection, sexual_orientation, race, income, living_status, 
                                        grew_up, occupations, prev_speech_therapy, 
                                        other_therapy, hearing_loss, hearing_aid, aphasia_cause, 
                                        aphasia_onset, brain_location, medications, filled_by, 
                                        completed_date, patient_info):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Membership_Enrollment_Form (
            sexual_orientation, race, income, living_status, grew_up, occupations, 
            prev_speech_therapy, other_therapy, hearing_loss, hearing_aid, aphasia_cause, 
            aphasia_onset, brain_location, medications, filled_by, completed_date, patient_info
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            sexual_orientation, race, income, living_status, grew_up, occupations, 
            prev_speech_therapy, other_therapy, hearing_loss, hearing_aid, aphasia_cause, 
            aphasia_onset, brain_location, medications, filled_by, completed_date, patient_info
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid
    
    def insert_medical_history_form(connection, physician_name, specialty, physician_address, physician_phone, 
                                    aphasia_cause, aphasia_onset, stroke_location, lesion_location, 
                                    primary_diagnosis, secondary_diagnosis, seizure_history, last_seizure_date, 
                                    anti_seizure_med, visual_impairments, 
                                    visual_field_cut, other_visual_impairments, completion_date, other_medical_conditions):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Medical_History_Form (
            physician_name, specialty, physician_address, physician_phone, aphasia_cause, aphasia_onset, 
            stroke_location, lesion_location, primary_diagnosis, secondary_diagnosis, seizure_history, 
            last_seizure_date, anti_seizure_med, visual_impairments, 
            visual_field_cut, other_visual_impairments, completion_date, other_conditions
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            physician_name, specialty, physician_address, physician_phone, aphasia_cause, aphasia_onset, 
            stroke_location, lesion_location, primary_diagnosis, secondary_diagnosis, seizure_history, 
            last_seizure_date, anti_seizure_med, visual_impairments, 
            visual_field_cut, other_visual_impairments, completion_date, other_medical_conditions
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_incident_report(connection, incident_date, incident_location, persons_involved, description, action_taken):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Incident_Report (
            incident_date, incident_location, persons_involved, description, action_taken
        ) 
        VALUES (%s, %s, %s, %s, %s)
        """

        data = (
            incident_date, incident_location, persons_involved, description, action_taken
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_evaluation(connection, completed, administerer, test_type, date_administered):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Evaluation (
            completed, administerer, test_type, date_administered
        ) 
        VALUES (%s, %s, %s, %s)
        """

        data = (
            completed, administerer, test_type, date_administered
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_transportation_information(connection, bus_transport, bus_company, bus_contact_phone, picked_up,
                                        pickup_person, relationship_to_member, primary_phone, secondary_phone):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Transportation_Information (
            bus_transport, bus_company, bus_contact_phone, picked_up, pickup_person, 
            relationship_to_member, primary_phone, secondary_phone
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            bus_transport, bus_company, bus_contact_phone, picked_up, pickup_person, 
            relationship_to_member, primary_phone, secondary_phone
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_caregiver(
        connection, name, phone, email, relationship, date_contacted, notes, group_attending, 
        attending, caregiver_type, sex, race, occupations, support_group, covid_vaccine_date, 
        allergies, medications, participation, robly, enrollment_form, medical_history, 
        emergency_contact_one, emergency_contact_two, transport_info, member_id
    ):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Caregiver (
            name, phone, email, relationship, date_contacted, notes, group_attending, 
            attending, caregiver_type, sex, race, occupations, support_group, covid_vaccine_date, 
            allergies, medications, participation, robly, enrollment_form, medical_history, 
            emergency_contact_one, emergency_contact_two, transport_info, member_id
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            name, phone, email, relationship, date_contacted, notes, group_attending, 
            attending, caregiver_type, sex, race, occupations, support_group, covid_vaccine_date, 
            allergies, medications, participation, robly, enrollment_form, medical_history, 
            emergency_contact_one, emergency_contact_two, transport_info, member_id
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_emergency_contact(connection, name, relationship, day_phone, evening_phone, cell_phone, email, address, completion_date):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Emergency_Contact (
            name, relationship, day_phone, evening_phone, cell_phone, email, address, completion_date
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            name, relationship, day_phone, evening_phone, cell_phone, email, address, completion_date
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_volunteer(connection, name, phone, address, email, referral_source, background_check_date, 
                        video_watched_date, emergency_contacts, media_release, confidentiality, training_level):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Volunteer (
            name, phone, address, email, referral_source, background_check_date, 
            video_watched_date, emergency_contacts, media_release, confidentiality, training_level
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            name, phone, address, email, referral_source, background_check_date, 
            video_watched_date, emergency_contacts, media_release, confidentiality, training_level
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_application(connection, birthday, occupation, is_slp, relevant_experience, education, interests_skills_hobbies, 
                        languages_spoken, will_substitute, convicted_of_crime, application_date):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Applications (
            birthday, occupation, is_slp, relevant_experience, education, interests_skills_hobbies, 
            languages_spoken, will_substitute, convicted_of_crime, application_date
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            birthday, occupation, is_slp, relevant_experience, education, interests_skills_hobbies, 
            languages_spoken, will_substitute, convicted_of_crime, application_date
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid

    def insert_outreach(connection, contacted_date, staff_contacted, organization, org_type, outreach_type, target_location, 
                        num_people, robly, notes):
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Outreach (
            contacted_date, staff_contacted, organization, org_type, outreach_type, target_location, 
            num_people, robly, notes
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            contacted_date, staff_contacted, organization, org_type, outreach_type, target_location, 
            num_people, robly, notes
        )

        cursor.execute(insert_query, data)
        connection.commit()
        if connection:
            connection.close()
        return cursor.lastrowid