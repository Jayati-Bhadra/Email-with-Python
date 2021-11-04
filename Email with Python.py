from nylas import APIClient

nylas = APIClient(
    CLIENT_ID,
    CLIENT_SECRET,
    ACCESS_TOKEN,
)
draft = nylas.drafts.create()
draft.subject = "With Love, from Nylas"
draft.body = "This email was sent using the Nylas Email API. Visit https://nylas.com for details."
draft.to = [{'name': 'My Nylas Friend', 'email': 'swag@nylas.com'}]  
from nylas import APIClient

nylas = APIClient(
    CLIENT_ID,
    CLIENT_SECRET,
    ACCESS_TOKEN,
)

draft = nylas.drafts.create()
draft.subject = "With Love, from Nylas"
draft.body = "This email was sent using the Nylas Email API. Visit https://nylas.com for details."


draft.to = [{'name': 'My Nylas Friend', 'email': 'swag@nylas.com'}]

draft.send()
thread = nylas.threads.get('{id}')
draft = thread.create_reply()
draft.body = "This is my reply"
draft.to = thread.from_
draft.cc = thread.cc
draft.bcc = thread.bcc
draft.send()
 from nylas import APIClient
    nylas = APIClient(
        CLIENT_ID,
        CLIENT_SECRET,
        ACCESS_TOKEN
    )
    
    thread = nylas.threads.get('{id}')
    draft = thread.create_reply()
    draft.body = "This is my reply"
    draft.to = thread.from_
    draft.cc = thread.cc
    draft.bcc = thread.bcc
    draft.send()
     attachment = open('attachment.pdf', 'r')
    file = nylas.files.create()
    file.filename = 'attachment.pdf'
    file.stream = attachment
    file.save()
    attachment.close()
     draft = nylas.drafts.create()
    draft.subject = "With Love, From Nylas"
    draft.body = 'This email was sent using the Nylas Email API. Visit https://nylas.com for details.'
    draft.to = [{'name': 'My Nylas Friend', 'email': 'swag@nylas.com'}]
    draft.attach(file)
    draft.send()
    from nylas import APIClient
    nylas = APIClient(
        CLIENT_ID,
        CLIENT_SECRET,
        ACCESS_TOKEN
    )
    
    
    attachment = open('attachment.pdf', 'r')
    file = nylas.files.create()
    file.filename = 'attachment.pdf'
    file.stream = attachment
    
    file.save()
    attachment.close()
    
    
    draft = nylas.drafts.create()
    draft.subject = "With Love, From Nylas"
    draft.body = 'This email was sent using the Nylas Email API. Visit https://nylas.com for details.'
    draft.to = [{'name': 'My Nylas Friend', 'email': 'swag@nylas.com'}]
    draft.attach(file)
    draft.send()
    
