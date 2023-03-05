# for add in vacancy search in db tables
import pandas

admin_database = 'admin_last_session'
archive_database = 'archive'
shorts_session_database = 'short_session_numbers'
admin_copy = 'admin_copy'
last_autopushing_time_database = 'last_autopushing_time'
short_session_database = 'shorts_session_name'
admin_table_fields = "id, chat_name, title, body, profession, vacancy, vacancy_url, company, english, relocation, " \
                     "job_type, city, salary, experience, contacts, time_of_public, created_at, agregator_link, " \
                     "session, sended_to_agregator, sub, tags, full_tags, full_anti_tags, short_session_numbers, " \
                     "level, approved, closed"

profession_table_fields = "id, chat_name, title, body, profession, vacancy, vacancy_url, company, english, relocation, " \
                             "job_type, city, salary, experience, contacts, time_of_public, created_at, agregator_link, " \
                             "session, sub, tags, full_tags, full_anti_tags, short_session_numbers, level, approved"


fields_admin_temporary = "id_admin_channel, id_admin_last_session_table, sended_to_agregator"

additional_elements = {'admin_last_session', 'archive'}

valid_professions = ['junior', 'backend', 'frontend', 'qa', 'devops', 'designer', 'game', 'mobile', 'product', 'pm', 'analyst',
                     'marketing', 'sales_manager', 'hr']
valid_professions_extended = []
valid_professions_extended.extend(valid_professions)
valid_professions_extended.extend(['fullstack'])
tables_for_search_vacancy_existing = [admin_database, 'archive']
# all_tables_for_vacancy_search = ['designer', 'game', 'product', 'mobile', 'pm', 'sales_manager', 'analyst', 'frontend',
#                      'marketing', 'devops', 'hr', 'backend', 'qa', 'junior', admin_database, archive_database]

profession_list_for_pushing_by_schedule = ['qa', 'devops', 'mobile', 'game', 'frontend', 'backend', 'marketing']
all_tables_for_vacancy_search = []
all_tables_for_vacancy_search.extend([admin_database, archive_database])
all_tables_for_vacancy_search.extend(valid_professions)

not_lower_professions = ['pm', 'game', 'designer', 'hr', 'analyst', 'qa', 'ba' 'devops', 'product']

white_admin_list = [1763672666, 556128576, 758905227, 945718420, 5755261667, 5884559465]

id_owner = 1763672666

#admin database name
channel_id_for_shorts = -1001671844820

# message_for_send = f'<i>Функционал дайджеста находится в состоянии альфа-тестирования, приносим свои ' \
#                                    f'извинения, мы работаем над тем чтобы вы получали информацию максимально ' \
#                                    f'качественную и в сжатые сроки</i>\n\n'

dict_for_title_shorts = {
    '': 'Системных аналитиков',
}

flood_control_logs_path = "./excel/flood_control.txt"
pattern_path = "./excel/pattern.txt"
admin_check_file_path = './logs/check_file.txt'
path_log_check_profession = "./excel/send_log_txt.txt"
report_file_not_actual_vacancy = "./excel/not_actual_vacancies.txt"

sites_search_words = ['designer', 'ui', 'junior', 'стажер', 'стажировка', 'product manager', 'project manager', 'python', 'php']

table_list_for_checking_message_in_db = ['admin_last_session', 'archive']

pre_message_for_shorts = '<i>Функционал дайджеста находится в состоянии альфа-тестирования, приносим свои ' \
                                   f'извинения, мы работаем над тем чтобы вы получали информацию максимально ' \
                                   f'качественную и в сжатые сроки</i>\n\n'

message_not_access = "Sorry, you have not the permissions"
path_last_pattern = "./patterns/last_changes/pattern_Alex2809 (6).py"
path_data_pattern = "./patterns/data_pattern/_data_pattern.py"

path_filter_error_file = "./excel/filter_jan_errors.txt"
db_fields_for_update_in_parsing = ['job_type', 'relocation', 'city', 'experience', 'english']

cities_file_path = './utils/additional_data/data.xlsx'
# cities_file_path = './../utils/additional_data/data.xlsx' # for tests
callback_for_push_shorts = ['*', 'all']

excel_data_df = pandas.read_excel(f'{cities_file_path}', sheet_name='Cities')
excel_dict = {
    'city': excel_data_df['city'].tolist(),
    'country': excel_data_df['country'].tolist(),
}
result_excel_dict = {}
for i in range(0, len(excel_dict['city'])):
    if excel_dict['country'][i] in result_excel_dict:
        result_excel_dict[excel_dict['country'][i]].append(excel_dict['city'][i])
    else:
        result_excel_dict[excel_dict['country'][i]] = [excel_dict['city'][i]]

clear_vacancy_trash_pattern = "[Ии]щем в команду[:]?|[Тт]ребуется[:]?|[Ии]щем[:]?|[Вв]акансия[:]?|[Пп]озиция[:]?|" \
                              "[Дд]олжность[:]|в поиске[:]|[Нн]азвание вакансии[:]|[VACANCYvacancy]{7}[:]?|[Pp]osition[:]?"

how_much_pages = 7
path_post_request_file = "./excel/path_post_request_file.txt"
till = 5
vacancy_fresh_time_days = 7
path_to_excel = "./excel/"
path_push_shorts_report_file = "./excel/report_push_shorts.txt"
tables_list_for_report = ['junior', '*']
developer_chat_id = 5884559465

post_request_for_example = {
    'profession': '',
    'specialization':
    'frontend',
    'programmingLanguage': ['js'],
    'technologies': ['react'],
    'level': ['all', 'trainee', 'entry level', 'junior', 'midle', 'senior', 'director', 'lead'],
    'country': 'BY',
    'city': '',
    'state': '',
    'salary': ['200', '400'],
    'salaryOption': ['hourly', 'perMonth', 'perYear', 'beforeTaxes', 'inHand'],
    'companyScope': '',
    'typeOfEmployment': ['all', 'fulltime', 'parttime', 'tempJob', 'contract', 'freelance', 'internship', 'volunteering'],
    'companyType': ['all', 'product', 'outsourcing', 'outstaff', 'consulting', 'notTechnical', 'startup'],
    'companySize': ['1-200', '201-500', '501-1000', '1000+'],
    'job_type': ['remote']
}

help_text = '/log or /logs - get custom logs (useful for developer\n' \
            '/get_participants - ❗️get the channel follower numbers\n' \
            '/delete_till - ❗️delete old vacancy from admin DB till date\n\n' \
            '------------ FOR DEVELOPER: ------------\n' \
            '⛔️/debugs\n' \
            '⛔️/developing\n' \
            '⛔️/get_tables_and_fields\n' \
            '⛔️/get_vacancy_names - you type the profession and bot shows you all titles\n' \
            '⛔️/add_tags_to_DB - (one time usable)\n' \
            '⛔️/rollback_last_short_session - one step back (shorts) you type number short_session (you can see)\n' \
            '⛔️/rollback_by_number_short_session - one step back (shorts) you type number short_session (you can see)\n' \
            '⛔️/get_vacancies_name_by_profession - get vacancies name from DB to file with fields\n' \
            '⛔️/ --- refresh_pattern - to get the modify pattern from DB\n' \
            '⛔️/get_and_write_level - define field level and rewrite to admin DB\n' \
            '⛔️/get_from_admin - get all vacancy_names from admin channel\n' \
            '⛔️/add_field_into_tables_db - type name and field type\n\n' \
            '⛔️/copy_prof_tables_to_archive_prof_tables - type name and field type\n\n' \
            '⛔️/peerchannel - useful for a developer to get id channel\n' \
            '⛔️/getdata - get channel data\n' \
            '⛔️/check_parameters - get vacancy\'s parameters\n' \
            '⛔️/get_backup_db - receive last db backup\n' \
            '⛔️/check_link_hh - doesnt work :)\n' \
            '⛔️/get_participants\n' \
            '⛔️/get_user_data\n' \
            '⛔️/emergency_push\n' \
            '⛔️/get_pattern\n' \
            '⛔️/get_pattern_pseudo\n' \
            '⛔️/clear_db_table\n' \
            '⛔️/numbers_of_archive\n' \
            '⛔️/get_flood_error_logs\n' \
            '⛔️/how_many_records_in_db_table - shows quantity of records in db table\n' \
            '⛔️/get_vacancy_for_example - receivw the random vacancy from admin\n' \
            '⛔️/get_vacancy_from_backend - random vacancy from backend\n' \
            '⛔️/add_and_push_subs - add subs and fill them\n' \
            '⛔️/get_random_vacancy_by_profession \n' \
            '⛔️/get_post_request \n' \
            '⛔️/rewrite_additional_db_fields - like job_type, english, experience, relocation, city\n' \
            '⛔️/show_db_records - random vacancy from db\n' \
            '⛔️/get_channel_members - get user\'s channels name\n' \
            '⛔️/transpose_no_sort_to_archive - all no_sort to archive\n' \
            '----------------------------------------------------\n\n' \
            '---------------- FILES: ----------------\n' \
            '/report_push_shorts - shorts report \n' \
            '----------------------------------------------------\n\n' \
            '---------------- PARSING: ----------------\n' \
            '🔆/magic_word - input word and get results from hh.ru\n' \
            '🔆/hh_kz - input word and get results from hh.ru\n' \
            '🔆/svyazi - get data from svyazi.app\n' \
            '🔆/finder - get the data from finder.vc\n' \
            '🔆/habr - get the data from career.habr.com\n' \
            '🔆/superjob - get the data from superjob.ru\n' \
            '🔆/rabota - get the data from rabota.by\n' \
            '🔆/dev - get the data from dev.by\n' \
            '🔆/geek - get data from geek.ru\n' \
            '🔆/remotehub - get data from www.remotehub.com\n' \
            '🔆/remotejob - get data from remote-job.ru\n' \
            '🔆/ingame - get data from ingame\n' \
            '🔆/praca - get data from praca.by\n' \
            '---------------------------------------------------\n\n' \
            '/download - ❗️you get excel from admin vacancies with search tags\n' \
            '/ambulance - if bot gets accident in hard pushing and you think you loose the shorts\n' \
            '/check_vacancies_for_relevance - to mark not actual vacancies id DB (closed will be TRUE)\n\n' \
            '---------------- TOOLS: ----------------\n' \
            '🛠/edit_pattern - stop proccess\n' \
            '/db_check_url_vacancy - does vacancy exist by link\n' \
            '/schedule - non-stop parsing\n' \
            '/restore_from_admin - restory the lost vacancies\n' \
            '/invite_people - start to invite followers\n' \
            '/get_news - start to invite followers\n' \
            '🖐️/stop - stop process\n' \
            '➡️/refresh_and_save_changes - One click for the correct refresh. Includes:\n' \
            '✅/refresh - to get the professions in excel format in all vacancies throgh the new filters logic (without rewriting)\n' \
            '✅/check_doubles - remove the vacancy"s doubles\n' \
            '✅/remove_completed_professions - remove complete professions\n' \
            '---------------------------------------------------\n\n' \
            '---------------- STATISTICS: ----------------\n' \
            '/how_many_vacancies_published - get the statistic file (created by Anna)\n' \
            '/how_many_vacancies_total - new report (created by Anna)\n' \
            '/vacancies_from - how many juniors have been written today and tomorrow\n' \
            '/check_title_body\n' \
            '/get_profession_parsing_tags_log - send the file with tags and antitags' \
            '/add_statistics\n\n' \
            '---------------------------------------------------\n\n' \
            '---------------- PUSHING BY SCHEDULE: ----------------\n' \
            '/hard_pushing_by_schedule - run pushing by schedule\n' \
            '/pick_up_forcibly_from_admin - if vacancies has been sent to the admin channel already and code has stopped\n' \
          '---------------------------------------------------\n\n' \
            '❗️- it is admin options'