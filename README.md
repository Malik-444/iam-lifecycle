<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
 
</head>
<body>
  <h1>🚀 Azure AD Identity Lifecycle Automation</h1>

  <p>Automated user provisioning and deprovisioning in Azure AD using Microsoft Graph API and Python.</p>

  <p>This project simulates an enterprise-grade identity lifecycle solution that can:</p>
  <ul>
    <li>Create new users (joiners)</li>
    <li>Update user attributes (movers)</li>
    <li>Disable or remove users (leavers)</li>
  </ul>

  <h2>🚨 Enterprise Problem This Project Solves</h2>
  <p>Modern enterprises often struggle with identity lifecycle management:</p>
  <ul>
    <li>Delayed deprovisioning creates security risks and access creep</li>
    <li>Inconsistent user attribute updates lead to compliance issues</li>
    <li>Manual processes are error-prone and hard to audit</li>
  </ul>
  <p>This project automates these workflows, reducing human error, improving security posture, and ensuring audit readiness.</p>

  <h2>🛡 Zero Trust Alignment</h2>
  <p>This project aligns with core <strong>Zero Trust security principles</strong>, where identity is the primary security boundary.</p>
  <ul>
    <li><strong>Verify explicitly:</strong> Users and access rights are validated automatically against Azure AD.</li>
    <li><strong>Least privilege:</strong> Access is granted and revoked according to lifecycle events.</li>
    <li><strong>Assume breach:</strong> Automated logging and monitoring enable rapid detection and mitigation.</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <pre>
fastapi_project/
├─ users.csv          # Mock CSV with sample users
├─ main.py            # Python script for automation
├─ README.md          # Project documentation
└─ lifecycle.log      # Logging of automated actions
  </pre>

  <h2>💻 Technologies Used</h2>
  <ul>
    <li>Python 3.x</li>
    <li>Microsoft Graph API</li>
    <li>Azure Active Directory (Entra ID)</li>
    <li>Logging and CSV processing</li>
  </ul>

  <h2>⚡ How to Run</h2>
  <ol>
    <li>Clone the repository</li>
    <li>Install required packages:
      <pre>pip install -r requirements.txt</pre>
    </li>
    <li>Fill in your Azure AD app credentials in <code>.env</code></li>
    <li>Run the script:
      <pre>python main.py</pre>
    </li>
    <li>Check <code>lifecycle.log</code> for automated actions</li>
  </ol>

  <h2>📊 Logging & Auditing</h2>
  <p>All lifecycle events are logged to <code>lifecycle.log</code> for auditing purposes, including:</p>
  <ul>
    <li>Users successfully created</li>
    <li>Users updated</li>
    <li>Users disabled or removed</li>
    <li>Errors such as user already exists or cannot disable</li>
  </ul>

  <h2>🎯 Key Takeaways</h2>
  <ul>
    <li>Automates repetitive IAM tasks in enterprise Azure AD environments</li>
    <li>Reduces human error and improves security posture</li>
    <li>Provides a reusable framework for real-world identity lifecycle management</li>
  </ul>

  <p>By presenting this project in your resume or portfolio, you demonstrate:</p>
  <ul>
    <li>Hands-on Azure IAM skills</li>
    <li>Automation and scripting for identity governance</li>
    <li>Alignment with Zero Trust and enterprise security standards</li>
  </ul>
</body>
</html>
