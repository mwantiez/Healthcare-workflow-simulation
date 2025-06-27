# Matt Wantiez
# ehr_workflow_simulation.py

import time

def log_step(step):
    print(f"[{time.strftime('%H:%M:%S')}] {step}")

def simulate_visit():
    log_step("Patient checks in at front desk (PMS)")
    time.sleep(1)
    
    log_step("Medical assistant takes vitals and updates EHR")
    time.sleep(1)
    
    log_step("Provider reviews history and documents chief complaint")
    time.sleep(1)
    
    log_step("Provider enters orders: Lab (LIS) and Imaging (RIS)")
    time.sleep(1)
    
    log_step("HL7 ORU^R01 message sent from LIS to EHR with lab results")
    time.sleep(1)
    
    log_step("CDSS flags abnormal result and notifies provider")
    time.sleep(1)
    
    log_step("Provider documents diagnosis (ICD-10) and procedure (CPT)")
    time.sleep(1)
    
    log_step("Billing department receives codes via PMS")
    time.sleep(1)
    
    log_step("Patient receives follow-up instructions and exits")
    time.sleep(1)

if __name__ == "__main__":
    print("Starting EHR Workflow Simulation...\n")
    simulate_visit()
    print("\nSimulation complete.")
