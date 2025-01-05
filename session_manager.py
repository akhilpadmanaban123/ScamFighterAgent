import time

active_sessions = {}

def start_scam_check(user_id, scam_type):
    active_sessions[user_id] = {
        "scam_type": scam_type,
        "question_index": 0,
        "responses": [],
        "start_time": time.time()
    }

def get_session(user_id):
    return active_sessions.get(user_id)

def update_session(user_id, response):
    if user_id in active_sessions:
        active_sessions[user_id]["responses"].append(response)
        active_sessions[user_id]["question_index"] += 1

def end_session(user_id):
    if user_id in active_sessions:
        del active_sessions[user_id]

def check_session_timeout(user_id):
    if user_id in active_sessions:
        session = active_sessions[user_id]
        if time.time() - session["start_time"] > 1200:  # 20 minutes
            end_session(user_id)
            return True
    return False