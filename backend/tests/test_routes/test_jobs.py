import json


def test_create_job(client,normal_user_token_headers):   #added normal_user_token_headers
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post("/jobs/create-job/",data=json.dumps(data),headers=normal_user_token_headers)  #added header in the post request
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"
 
# We need to modify each and every unit test in which we are making a post/delete request. Since we are not restricting get requests. We do not need headers for get requests.

def test_retrieve_job_by_id(client):
    data = {
        "title":"SDE 1 Yahoo",
        "company":"testhpp",
        "company_url":"https://www.fdj.com",
        "location":"USA, NY",
        "description":"Testing",
        "data_posted":"2022-07-20"
        }
    client.post("/job/create-job",json.dumps(data))
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"
