"""
data.py

File with all the Data details
"""

class WebData:
    """
    WebData Class contains all data that is required for testing
    """

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.forgetUsername = "Admin"
        self.username = "Admin"
        self.password = "admin123"
        self.title = "OrangeHRM"
        self.pwsentURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
        self.adminHeaders = "User Management\nJob\nOrganization\nQualifications\nMore"
        self.adminMenu = 'Admin\n' 'PIM\n' 'Leave\n' 'Time\n' 'Recruitment\n' 'My Info\n' 'Performance\n' 'Dashboard\n' 'Directory\n' 'Maintenance\n' 'Claim\n' 'Buzz'