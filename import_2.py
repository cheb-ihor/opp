from opp_dod import Admin
admin = Admin("John", "Doe", 30, 
              ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"])
admin.privileges.show_privileges()