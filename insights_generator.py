import pandas as pd
from datetime import datetime

def generate_insights(file_path="user_behavior_log.csv"):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        if df.empty:
            print("No data found.")
            return

        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'], format="%d-%m-%Y %H:%M")
        df['hour'] = df['timestamp'].dt.hour

        # Insight 1: Completion rate
        total = len(df)
        completed = len(df[df['status'] == 'completed'])
        skipped = len(df[df['status'] == 'skipped'])
        repeated = len(df[df['status'] == 'repeated'])

        completion_rate = round((completed / total) * 100, 2)

        # Insight 2: Most productive hour
        productive_hours = df[df['status'] == 'completed']['hour'].mode()
        productive_hour = productive_hours[0] if not productive_hours.empty else "No data"

        # Insight 3: Most skipped task
        most_skipped = df[df['status'] == 'skipped']['task_name'].mode()
        skipped_task = most_skipped[0] if not most_skipped.empty else "None"

        # Insight 4: Most repeated task
        most_repeated = df[df['status'] == 'repeated']['task_name'].mode()
        repeated_task = most_repeated[0] if not most_repeated.empty else "None"

        # Show results
        print("\n📊 Behavioral Insights:")
        print(f"✅ Completion Rate: {completion_rate}%")
        print(f"⏰ Most Productive Hour: {productive_hour}:00")
        print(f"📌 Most Skipped Task: {skipped_task}")
        print(f"🔁 Most Repeated Task: {repeated_task}")

        # Suggestion
        if isinstance(productive_hour, int):
            print(f"\n💡 Suggestion: You seem most productive around {productive_hour}:00. Try scheduling important tasks during that time.")

        # Save insights to CSV
        insights_data = {
            'metric': ['completion_rate', 'most_productive_hour', 'most_skipped_task', 'most_repeated_task'],
            'value': [f"{completion_rate}%", f"{productive_hour}:00", skipped_task, repeated_task]
        }

        insights_df = pd.DataFrame(insights_data)
        insights_df.to_csv("insights_report.csv", index=False)
        print("\n✅ Insights saved to insights_report.csv")

    except Exception as e:
        print("Error generating insights:", e)

# Run the insights generator
if __name__ == "__main__":
    generate_insights()
