# Google Calendar Free Time Finder

This application allows users to find overlapping free time slots among multiple Google Calendar users. It uses the Google Calendar API to query users' calendar events and calculates the free time slots based on their busy events.

## Requirements

- Python 3.6+
- Google API Client Library for Python
- Google Auth Library for Python

Install the required packages with `pip`:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

## `User`

A class that represents a user's calendar information, including their credentials, primary calendar, time zone, and the number of days for the free/busy window.

## Functions

The following functions are available for use:

### `authenticate_user(TOKENS_FILE_PATH)`

Authenticates a user, asks for Google Calendar permissions, and saves their credentials according to their Google ID.

### `get_credentials_by_google_id(google_id, tokens_file_path)`

Reads the JSON file and returns the corresponding content for the given Google ID.



### `find_overlapping_free_blocks(viewer_user, users_list)`

Finds overlapping free time blocks among a list of users.

## Usage

1. Authenticate the users using `authenticate_user()` function. This will save the user's credentials in a JSON file with their Google ID.

```python
authenticate_user()
```

2. Retrieve the user's credentials using their Google ID.
  ```python
  c1 = get_credentials_by_google_id("user_key_one_from_json", TOKENS_FILE_PATH)
  c2 = get_credentials_by_google_id("user_key_one_from_json", TOKENS_FILE_PATH)
  ```
  
 3. Create User objects for each user using their credentials, primary calendar settings, time zone, and the number of days for the free/busy window.
  ```python
  u1 = User(primary_only=True,
        time_zone_str='Africa/Cairo',
        window_days=1,
        credentials=c1)

  u2 = User(primary_only=True,
            time_zone_str='Africa/Cairo',
            window_days=1,
            credentials=c2)
   ```
 4. Use the find_overlapping_free_blocks(viewer_user, users_list) function to find overlapping free time blocks among a list of users.
  ```python
  find_overlapping_free_blocks(viewer_user=u1, users_list=[u1, u2])
  ```
This function will return a list of overlapping free time blocks among the users.


## Example

The following code demonstrates how to authenticate users, retrieve their credentials, create User objects, and find overlapping free time blocks:
```python
from free_time_finder import authenticate_user, get_credentials_by_google_id, User, find_overlapping_free_blocks

TOKENS_FILE_PATH = "user_tokens.json"
```

# Authenticate users and save their credentials
```python
authenticate_user()
```

# Retrieve user credentials
```python
c1 = get_credentials_by_google_id("user_key_one_from_json", TOKENS_FILE_PATH)
c2 = get_credentials_by_google_id("user_key_one_from_json", TOKENS_FILE_PATH)
```

# Create User objects
```python
u1 = User(primary_only=True,
          time_zone_str='Africa/Cairo',
          window_days=1,
          credentials=c1)

u2 = User(primary_only=True,
          time_zone_str='Africa/Cairo',
          window_days=1,
          credentials=c2)
```
# Find overlapping free time blocks
```python
result = find_overlapping_free_blocks(viewer_user=u1, users_list=[u1, u2])
print(result)
```




    

    



