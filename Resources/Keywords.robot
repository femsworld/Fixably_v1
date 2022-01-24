*** Setting ***
Documentation     Register New users, login and review user details
Library           SeleniumLibrary
Library           FakerLibrary
Resource          ../Resources/Variables.robot


*** Keywords ***

Obtain API token
     Create Session  ObtainToken      ${Base_URL}
     ${Data}=   Create dictionary    Code=${Access_Code}
     #${headers}=   Create dictionary    Context-Type=application/JSON
     #${resp}=  post request    ObtainToken    /token       headers= ${headers}      data=${Data}
     ${resp}=  POST On Session   ObtainToken    /token       data=${Data}    #headers= ${headers}
     ${Token}=    evaluate       $resp.json().get("token")
     log to console  ${resp.status_code}
     log to console  ${resp.content}