from openai import OpenAI
import os
import time

MEDICAL_ASSISTANT_ID = "asst_kbnbavMxcBXfIrNWGcDCtaat"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )


def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")

def create_thread_and_run(user_input):
  thread = client.beta.threads.create()
  run = submit_message(MEDICAL_ASSISTANT_ID, thread, user_input)
  return thread, run



# # Testing code:
# thread1, run1 = create_thread_and_run(
#   "I have been diagnosed with pancreatic cancer, what does this mean for me?"
# )

# Pretty printing helper
def pretty_print(messages):
    message = []
    for m in messages:
        message.append(f"{m.content[0].text.value}")
    return message[-1]


# Waiting in a loop
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


# # Wait for Run 1
# run1 = wait_on_run(run1, thread1)
# pretty_print(get_response(thread1))

# run1 = submit_message(MEDICAL_ASSISTANT_ID, thread1, "Thank you for your help")
# run1 = wait_on_run(run1, thread1)

# pretty_print(get_response(thread1))

