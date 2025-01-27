

# configures user detection
def detectUser(user):
    # Check if the user is a superuser
    if user.is_superadmin or user.is_superuser:
        return '/admin'

    # Check if the user is a regular user
    elif user.role == 1:
        return 'calculator'

    # Fallback
    else:
        return '/'



    
    
    
     
    
        
    
   