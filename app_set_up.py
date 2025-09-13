from transformers import pipeline
import datetime
import random
quiz_bot = pipeline("text-generation", model="gpt2")
motivate_bot = pipeline("text-generation", model="gpt2")
user_data = {
    "streak": 0,
    "last_date": None,
    "score": 0
}
def update_streak():
    today = datetime.date.today()
    if user_data["last_date"] == today:
        print(f"🔥 Already studied today! Streak: {user_data['streak']} days")
    elif user_data["last_date"] == today - datetime.timedelta(days=1):
        user_data["streak"] += 1
        user_data["last_date"] = today
        print(f"✅ Streak continued! You're on fire: {user_data['streak']} days")
    else:
        user_data["streak"] = 1
        user_data["last_date"] = today
        print("🔁 Streak reset. But you're back—let’s go!")
def generate_quiz(topic):
    prompt = f"Ask a short quiz question about {topic} with answer."
    result = quiz_bot(prompt, max_length=50, do_sample=True)[0]['generated_text']
    print("🧠 Quiz Time:")
    print(result)
    correct = random.choice([True, False])
    if correct:
        user_data["score"] += 1
        print("✅ Correct! Score:", user_data["score"])
    else:
        print("❌ Oops! Try again. Score:", user_data["score"])


def send_motivation():
    prompt = "Give a short motivational quote for students."
    quote = motivate_bot(prompt, max_length=50, do_sample=True)[0]['generated_text']
    print("💜 Motivation:")
    print(quote)
update_streak()
generate_quiz("Boolean algebra")
send_motivation()