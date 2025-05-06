# Data (all manually coded)
countries_by_budget = {
    "low": ["Thailand", "Indonesia", "Vietnam"],
    "medium": ["Italy", "Greece", "Turkey"],
    "high": ["France", "Switzerland", "Maldives"]
}

activities_by_country = {
    "Thailand": "Island boat tour with a sunset view",
    "Indonesia": "Private beach picnic in Bali",
    "Vietnam": "Couple’s spa in Da Nang",
    "Italy": "Gondola ride in Venice",
    "Greece": "Cliffside dinner in Santorini",
    "Turkey": "Hot air balloon ride in Cappadocia",
    "France": "Private Eiffel Tower dinner",
    "Switzerland": "Luxury train ride through the Alps",
    "Maldives": "Underwater restaurant dinner and stay"
}

# Functions
def predict_partner_gender(user_gender):
    if user_gender.lower() == "male":
        return "female"
    elif user_gender.lower() == "female":
        return "male"
    else:
        return "female"  # default

def choose_country(budget_level):
    options = countries_by_budget.get(budget_level.lower())
    if not options:
        print("Invalid budget. Defaulting to 'low'.")
        options = countries_by_budget["low"]

    print("\nBased on your budget, here are 3 countries you can propose in:")
    for idx, country in enumerate(options, 1):
        print(f"{idx}. {country}")

    while True:
        try:
            choice = int(input("Select a country (1/2/3): "))
            if 1 <= choice <= 3:
                return options[choice - 1]
            else:
                print("Please select 1, 2, or 3.")
        except:
            print("Invalid input. Enter a number.")

def build_timeline(country, partner_name):
    print(f"\n💖 Your Romantic Proposal Timeline in {country} 💖\n")
    print("🕐 08:00 AM - Arrive at airport and check-in")
    print("🛫 10:00 AM - Flight departs")
    print("🛬 02:00 PM - Land in", country)
    print("🏨 03:30 PM - Check into a luxury hotel")
    print("🎁 05:00 PM - Surprise gift for", partner_name)
    print(f"🌇 06:30 PM - Romantic activity: {activities_by_country[country]}")
    print("🍽️ 08:00 PM - Candlelight dinner with violin music")
    print(f"💍 09:00 PM - Proposal moment! Ask {partner_name} the big question 💖")
    print("🌙 10:30 PM - Relax under the stars and celebrate the moment")

def romantic_planner():
    print("💖 Welcome to the Romantic Experience Planner 💖\n")

    user_gender = input("What's your gender? (male/female): ").strip().lower()
    partner_gender = predict_partner_gender(user_gender)

    partner_name = input("What's your partner's name? ").strip()

    while True:
        try:
            budget = input("What's your budget? (low/medium/high): ").strip().lower()
            if budget not in ["low", "medium", "high"]:
                print("Please enter 'low', 'medium', or 'high'.")
                continue
            break
        except:
            print("Invalid input. Try again.")

    selected_country = choose_country(budget)
    build_timeline(selected_country, partner_name)

# Run the planner
romantic_planner()
