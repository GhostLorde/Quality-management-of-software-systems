import requests

delete_pet_headers = {
    "auth_key": "003c6904c7f44a085a12f9bf146415bb3d72270254cfd4dc8e0bd1e2",
    "pet_id": "526c71d9-3787-4b72-b04f-da90293b869b"
}

delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "526c71d9-3787-4b72-b04f-da90293b869b"


def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(delete_pet(DELETE_pet_link, delete_pet_params, delete_pet_headers))
