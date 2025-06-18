def tickets():

    import requests
    import json
    # print(requests)

    url1=""
    url20_old="https://dev.api.gsk.com/servicenow/api/now/table/sc_task?sysparm_query=assignment_group.name=SAP-Workflow-L2^cat_item.sys_name=GP%26T ERP Operations L2 Routine Change^assigned_toISEMPTY&sysparm_suppress_pagination_header=true&sysparm_exclude_reference_link=true&sysparm_fields=number, short_description, assignment_group, variables.requestedfor_name, variables.routine_change, variables.service, variables.service_offering, variables.assignment_group, variables.incident_id, variables.incident_creation_date, variables.comments, variables.revtrak_rt_number, variables.expected_sla_due, variables.sla_met1&sysparm_limit=20&sysparm_display_value=true&active=true"
    url20_v1 = "https://dev.api.gsk.com/servicenow/api/now/table/sc_task?sysparm_query=active=true^assignment_group=95cb5a941bbe90901757773e0d4bcb2d^short_description=GP%26T ERP Operational Service Request - Fulfilment Task&sysparm_suppress_pagination_header=true&sysparm_exclude_reference_link=true&sysparm_limit=20&sysparm_display_value=true&active=true&sysparm_fields=number, short_description, assignment_group, variables.requestedfor_name, variables.to_user.user_name,request_type,variables.routine_change,variables.request_type,variables.document_no,variables.from_user,variables.to_user,variables.document_type,variables.status,,variables.expected_sla_due, variables.sla_met1"
    url20 = "https://dev.api.gsk.com/servicenow/api/now/table/sc_task?sysparm_query=active=true^assignment_group=95cb5a941bbe90901757773e0d4bcb2d^short_description=GP%26T ERP Operational Service Request - Fulfilment Task&sysparm_suppress_pagination_header=true&sysparm_exclude_reference_link=true&sysparm_limit=20&sysparm_display_value=true&active=true&sysparm_fields=number, short_description, assignment_group, request_item,request_item.opened_by,request_item.opened_by.email,variables.requestedfor_name, variables.to_user.user_name,request_type,variables.routine_change,variables.request_type,variables.document_no,variables.from_user,variables.to_user,variables.document_type,variables.status,,variables.expected_sla_due, variables.sla_met1"
    url20 = "https://dev.api.gsk.com/servicenow/api/now/table/sc_task?sysparm_query=active=true^assignment_group=95cb5a941bbe90901757773e0d4bcb2d^short_description=GP%26T ERP Operational Service Request - Fulfilment Task&sysparm_suppress_pagination_header=true&sysparm_exclude_reference_link=true&sysparm_limit=20&sysparm_display_value=true&active=true&sysparm_fields=number, short_description, assignment_group, request_item,request_item.opened_by,request_item.opened_by.email,variables.requestedfor_name, variables.to_user.user_name,request_type,variables.routine_change,variables.request_type,variables.document_no,variables.from_user,variables.to_user,variables.document_type,variables.status,,variables.expected_sla_due, variables.sla_met1"
    r = requests.get(url=url20,headers={'apikey':"MTMzYzcyYzctMGYzMC00NzVlLWI4ZmItNGYwMzJkZWZmNDQ2DYdocw7tkiQIUFiKPYbe04JlYltU2YhPYlGQFvw0IY4e"})

    print(r)
    val=r.content
    f=json.loads(val)
    # print(f)
    # li=[f['result'][i]["variables.routine_change"] for i in range(len(f['result']))]
    # print(len(f['result']))
    print(f)
    result = f['result']
    no_of_sctasks = len(result)

    cat_113 = {sctask['number']:{'request_item':sctask["request_item"],'opened_by':sctask["request_item.opened_by"],'opened_by_email':sctask["request_item.opened_by.email"],'docid':sctask["variables.document_no"],'uuser':sctask["variables.to_user.user_name"]} for sctask in result if '113' in sctask['variables.request_type']}

    cat_114 = {sctask['number']:{'request_item':sctask["request_item"],'opened_by':sctask["request_item.opened_by"],'opened_by_email':sctask["request_item.opened_by.email"],'docid':sctask["variables.document_no"],'uuser':sctask["variables.to_user.user_name"]} for sctask in result if '114' in sctask['variables.request_type']}

    cat_115 = {sctask['number']:{'request_item':sctask["request_item"],'opened_by':sctask["request_item.opened_by"],'opened_by_email':sctask["request_item.opened_by.email"],'docid':sctask["variables.document_no"],'uuser':sctask["variables.to_user.user_name"],'request_for':sctask["variables.requestedfor_name"]} for sctask in result if '115' in sctask['variables.request_type']}

    cat_116 = {sctask['number']:{'request_item':sctask["request_item"],'opened_by':sctask["request_item.opened_by"],'opened_by_email':sctask["request_item.opened_by.email"],'docid':sctask["variables.document_no"],'uuser':sctask["variables.to_user.user_name"]} for sctask in result if '116' in sctask['variables.request_type']}

    # cat_115 = [sctask['variables.request_type'] for sctask in result]
    print(cat_115)
    
    return {'cat_113':cat_113,'cat_114':cat_114,'cat_115':cat_115,'cat_116':cat_116}


# import requests

# Constants
# url = "https://gskdev.service-now.com/api/gskgs/service_catalog_task/Update_Task"
# task_id = "SCTASK2707302"
# client_id = "61dddd006c38a210b4fcfe3348a76489"
# client_secret = "GR!Q84VQ-8"
# username = "event_int_nexthink_dev"
# password = "Opend00r1nexthink!"

# # Get the access token
# token_url = "https://gskdev.service-now.com/oauth_token.do"
# token_data = {
#     "grant_type": "client_credentials",
#     "client_id": client_id,
#     "client_secret": client_secret,
# }

# response = requests.post(token_url, data=token_data)
# access_token = response.json().get("access_token")

# # Check if the token was retrieved successfully
# if access_token:
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "task_id": task_id,
#         "Content-Type": "application/json",
#     }
    
#     # Body of the PATCH request
#     body = {
#         "work_notes": "test update 123"
#     }
    
#     # Make the PATCH request
#     patch_response = requests.patch(url, headers=headers, json=body)
    
#     # Print the response
#     if patch_response.status_code == 200:
#         print("Task updated successfully:", patch_response.json())
#     else:
#         print("Error updating task:", patch_response.status_code, patch_response.text)
# else:
#     print("Failed to retrieve access token.")
