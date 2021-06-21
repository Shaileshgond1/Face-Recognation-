def SMS():
                
                            
                from twilio.rest import Client
                account_xyz = 'AC28e914dc084c3fc505166196421c8a87'
                auth_token = 'e77c27d5d60a2c7c73a7f9e11c9a0898'

                client = Client(account_xyz, auth_token)
                message = client.messages.create(
                                              from_='+14427776162',
                                              body ='Hello! This is python',
                                              to ='+918669040343'
                              )
