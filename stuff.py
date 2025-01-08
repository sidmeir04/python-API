# # id, staff, caller_name, caller_email, call_date, phone_number, referral_type, additional_notes, tour_scheduled, tour_not_scheduled_reason, follow_up_date
# dict_results = {}
# columns = ["id", "staff", "caller_name", "caller_email", "call_date", "phone_number", "referral_type", "additional_notes", "tour_scheduled", "tour_not_scheduled_reason", "follow_up_date"]
# for i in range(len(columns)):
#     dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]
# return dict_results