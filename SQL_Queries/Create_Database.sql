SET foreign_key_checks = 0;
DROP DATABASE adler_aphasia_center;
CREATE DATABASE adler_aphasia_center;
SET foreign_key_checks = 1;

USE adler_aphasia_center;
CREATE TABLE Contact (
    id INT AUTO_INCREMENT PRIMARY KEY,
    staff text,
    caller_name VARCHAR(50),
    caller_email VARCHAR(50),
    call_date DATE,
    phone_number VARCHAR(15),
    referral_type VARCHAR(50),
    additional_notes TEXT,
    tour_scheduled BOOLEAN,
    tour_not_scheduled_reason TEXT,
    follow_up_date DATE
);

CREATE TABLE Tour (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tour_date DATE,                  -- Date of the tour
    attended BOOLEAN,                -- Whether the person attended the tour
    no_join_reason TEXT,             -- Reason for not joining
    clinicians VARCHAR(50),          -- Clinicians who toured
    attendees TEXT,                  -- Who attended the tour
    interactions TEXT,               -- Interactions during the tour
    strategies_used BOOLEAN,         -- Whether strategies were used
    aep_deadline DATE,               -- Deadline to join AEP
    joined_after BOOLEAN,            -- Whether they joined after the tour
    likely_to_join BOOLEAN,          -- Likely to join after the tour
    additional_notes TEXT,
    canceled BOOLEAN,                -- Whether the tour was canceled
    cancel_reason TEXT               -- Reason for cancelation
);

CREATE TABLE Membership_Enrollment_Form (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sexual_orientation VARCHAR(20),
    race VARCHAR(50),
    income INT,
    living_status VARCHAR(50),                   -- Living status code
    grew_up VARCHAR(50),
    occupations TEXT,                    -- List of occupations
    prev_speech_therapy TEXT,            -- Previous speech therapy
    other_therapy TEXT,
    hearing_loss BOOLEAN,
    hearing_aid BOOLEAN,
    aphasia_cause VARCHAR(50),
    aphasia_onset DATE,                  -- Date of onset of aphasia
    brain_location VARCHAR(50),          -- Location in the brain affected
    medications TEXT,
    filled_by VARCHAR(50),               -- Filled out by
    completed_date DATE,                 -- Date completed
    patient_info JSON                    -- Detailed patient information
);

CREATE TABLE Medical_History_Form (
    id INT AUTO_INCREMENT PRIMARY KEY,
    physician_name VARCHAR(50),            -- Physician completing the form
    specialty VARCHAR(50),                 -- Medical specialty
    physician_address VARCHAR(50),
    physician_phone VARCHAR(20),
    aphasia_cause VARCHAR(50),
    aphasia_onset DATE,                    -- Date of onset of aphasia
    stroke_location VARCHAR(50),
    lesion_location VARCHAR(50),
    primary_diagnosis VARCHAR(50),         -- Primary medical diagnosis
    secondary_diagnosis VARCHAR(50),       -- Secondary medical diagnosis
    seizure_history BOOLEAN,               -- History of seizures
    last_seizure_date DATE,                -- Date of last seizure
    anti_seizure_med BOOLEAN,              -- On anti-seizure medication
    visual_impairments TEXT,               -- Visual impairments
    visual_field_cut BOOLEAN,              -- Visual field cut present
    other_visual_impairments VARCHAR(50),  -- Additional visual impairments
    completion_date DATE,                  -- Date of completion
    other_conditions JSON                  -- Other medical conditions
);

CREATE TABLE Incident_Report (
    id INT AUTO_INCREMENT PRIMARY KEY,
    incident_date DATE,               -- Date of the incident
    incident_location VARCHAR(50),    -- Location of the incident
    persons_involved TEXT,            -- Persons involved in the incident
    description TEXT,                 -- Brief description of the incident
    action_taken TEXT                 -- Action taken following the incident
);

CREATE TABLE Evaluation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    completed BOOLEAN,                -- Whether the evaluation was completed
    administerer VARCHAR(50),         -- Who administered the evaluation
    test_type TEXT,                   -- Type of test administered
    date_administered DATE            -- Date the evaluation was administered
);

CREATE TABLE Transportation_Information (
    id INT AUTO_INCREMENT PRIMARY KEY,
    am_name VARCHAR(50),
    am_phone VARCHAR(20),
    pm_name VARCHAR(50),
    pm_phone VARCHAR(20),
    transportation_notes TEXT
);

CREATE TABLE Emergency_Contact (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),               -- Emergency contact's name
    relationship VARCHAR(50),        -- Relationship to the member
    day_phone VARCHAR(20),           -- Daytime phone number
    evening_phone VARCHAR(20),       -- Evening phone number
    cell_phone VARCHAR(20),          -- Cell phone number
    email VARCHAR(50),               -- Email address
    address VARCHAR(100),            -- Contact's address
    completion_date DATE             -- Date the form was completed
);

CREATE TABLE Member (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    -- age INT,
    dob DATE,                          -- Date of birth
    email VARCHAR(50),
    aep_completion_date DATE,          -- Date completed AEP
    join_date DATE,                    -- Date joined
    schedule INT,                      -- Schedule in weeks or other interval
    phone VARCHAR(20),
    address VARCHAR(50),
    county VARCHAR(50),
    gender CHAR(1),                    -- 'M' or 'F'
    veteran BOOLEAN,                   -- Veteran status
    joined BOOLEAN,                    -- Whether the member joined
    caregiver_needed BOOLEAN,          -- Whether a caregiver is needed
    adler_program VARCHAR(50),         -- Adler program info
    member_type VARCHAR(50),
    date_changed DATE,
    notes TEXT,
    member_info JSON,                  -- Detailed member information

    enrollment_form INT,
    FOREIGN KEY (enrollment_form) REFERENCES Membership_Enrollment_Form(id),
    medical_history INT,
    FOREIGN KEY (medical_history) REFERENCES Medical_History_Form(id),
    emergency_contact_one INT,
    emergency_contact_two INT,
    FOREIGN KEY (emergency_contact_one) REFERENCES Emergency_Contact(id),
    FOREIGN KEY (emergency_contact_two) REFERENCES Emergency_Contact(id),
    transport_info INT,
    FOREIGN KEY (transport_info) REFERENCES Transportation_Information(id)
);

CREATE TABLE Applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    birthday DATE,                    -- Applicant's birthday
    occupation VARCHAR(50),           -- Applicant's occupation
    is_slp BOOLEAN,                   -- Whether the applicant is a Speech-Language Pathologist (SLP)
    relevant_experience TEXT,         -- Work or relevant experiences
    education TEXT,                   -- Education details
    interests_skills_hobbies TEXT,    -- Interests, skills, and hobbies
    languages_spoken VARCHAR(100),    -- Languages spoken by the applicant
    will_substitute BOOLEAN,          -- Willingness to substitute
    convicted_of_crime BOOLEAN,      -- Whether the applicant has been convicted of a crime
    application_date DATE             -- Date of application
);

CREATE TABLE Volunteer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),                 -- Volunteer name
    phone VARCHAR(20),                -- Phone number
    address VARCHAR(50),              -- Volunteer address
    email VARCHAR(50),                -- Volunteer email
    referral_source TEXT,             -- Source of referral
    background_check_date DATE,       -- Date background check was completed
    video_watched_date DATE,          -- Date watched the orientation video
    emergency_contacts TEXT,          -- Emergency contacts
    media_release BOOLEAN,            -- Media release consent
    confidentiality BOOLEAN,          -- Confidentiality agreement
    training_level INT,               -- Training level (0-4)

    resumue int,
    FOREIGN KEY (resumue) REFERENCES Applications(id)
);

CREATE TABLE Caregiver (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),                -- Caregiver's name
    phone VARCHAR(20),               -- Phone number
    email VARCHAR(50),               -- Caregiver's email
    relationship VARCHAR(50),        -- Relationship to person with aphasia -
    date_contacted DATE,             -- Date contacted
    notes TEXT,                      -- Additional notes
    group_attending VARCHAR(50),     -- Group attending
    attending BOOLEAN,                -- Whether attending or not
	caregiver_type VARCHAR(50),      -- Type of caregiver
    sex CHAR(1),                     -- Sex of caregiver ('M' or 'F')
    race VARCHAR(50),                -- Race of caregiver
    occupations VARCHAR(150),        -- Caregiver's occupations
    support_group BOOLEAN,           -- Whether attending a support group
    covid_vaccine_date DATE,         -- Date of COVID vaccine
    allergies VARCHAR(100),          -- Allergies
    medications TEXT,                -- Medications
    participation TEXT,              -- Participation details
    robly BOOLEAN,                   -- If Robly is used for communication
    
    enrollment_form INT,
    FOREIGN KEY (enrollment_form) REFERENCES Membership_Enrollment_Form(id),
    medical_history INT,
    FOREIGN KEY (medical_history) REFERENCES Medical_History_Form(id),
    emergency_contact_one INT,
    emergency_contact_two INT,
    FOREIGN KEY (emergency_contact_one) REFERENCES Emergency_Contact(id),
    FOREIGN KEY (emergency_contact_two) REFERENCES Emergency_Contact(id),
    transport_info INT,
    FOREIGN KEY (transport_info) REFERENCES Transportation_Information(id),
    member_id INT,
    FOREIGN KEY (member_id) REFERENCES Member(id)
);

CREATE TABLE Outreach (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contacted_date DATE,              -- Date contacted
    staff_contacted VARCHAR(50),      -- Staff member contacted
    organization VARCHAR(50),         -- Name of the organization
    org_type VARCHAR(50),             -- Type of organization
    outreach_type VARCHAR(50),        -- Type of outreach conducted
    target_location VARCHAR(50),      -- Target location for outreach
    num_people INT,                   -- Number of people contacted
    robly BOOLEAN,                    -- If Robly was used for communication
    notes TEXT                        -- Additional notes regarding outreach
);