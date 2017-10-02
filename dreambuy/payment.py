from instamojo_wrapper import Instamojo
import requests

api_key = 'a3a3d3f308fb5cb4aa722f79c687c3fe'
auth_token = '675fd35d0a3015d49814a1e2e843e6d4'
api = Instamojo(api_key=api_key,
                auth_token=auth_token)

# # Create a new Payment Request
def mk_pymt(amt,purpose, usr,rurl,mblnum=None,mlid=None,):
    response = api.payment_request_create(
        amount=amt,
        purpose=purpose,
        buyer_name=usr,
        phone=mblnum,
        send_email=False,
        email=mlid,
        redirect_url=rurl
        )
    return response


def pymt_status(payment_request_id):
    headers = { "X-Api-Key": api_key, "X-Auth-Token": auth_token}
    response = requests.get("https://www.instamojo.com/api/1.1/payment-requests/"+str(payment_request_id)+"/",
      headers=headers)
    response = (response.json())

    return [response['payment_request']['purpose'],response['payment_request']['payments'][0]['status'],response['payment_request']['payments'][0]['amount']]

    # [response['payment_request']['payments'][0]['status'],response['payment_request']['payments'][0]['amount']]

