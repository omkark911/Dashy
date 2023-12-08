import requests

def fetch_facebook_data(access_token):
    # Get user profile information
    profile_url = f'https://graph.facebook.com/v13.0/me?fields=id,name,bio&access_token={access_token}'
    profile_response = requests.get(profile_url)
    profile_data = profile_response.json()

    # Get user posts
    posts_url = f'https://graph.facebook.com/v13.0/me/posts?fields=message,likes.summary(true),comments.summary(true),created_time&access_token={access_token}'
    posts_response = requests.get(posts_url)
    posts_data = posts_response.json()

    # Extract relevant information from the responses
    profile_info = {
        'name': profile_data.get('name'),
        'bio': profile_data.get('bio')
    }

    posts = []
    for post in posts_data.get('data', []):
        post_info = {
            'message': post.get('message'),
            'likes': post['likes']['summary']['total_count'],
            'comments': post['comments']['summary']['total_count'],
            'created_time': post['created_time']
        }
        posts.append(post_info)

    return profile_info, posts

# Example usage:
access_token = 'EAAMz03DbbgQBO4p7ZAwwf3d1qNRMh211INIHeoqZAqRrdDD2hfY2qh256VCGQzTMu4coq1bDS3YPoSg7YOJSTfJHBPOB2W78UXmEmQqDEdH1ZAZBpvnIN18QDOYHpYNSmHZCNNBX0CGMynsp9jmcSGAMbvpIWjktMFyGjxXi2jhAuxDtRhuUi5erF1uEv4lYWvJe9qybkJzzwxdmZCpL8cBIM99CsZD'
profile_info, posts = fetch_facebook_data(access_token)

# Print the results
print("Profile Information:", profile_info)
print("Posts:")
for post in posts:
    print(post)
