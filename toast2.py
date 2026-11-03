from plyer import notification

# Function to display a notification
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # The notification will stay for 10 seconds
    )

# Example usage
if __name__ == "__main__":
    show_notification("Hello!", "This notification is compatible with multiple desktop platforms.")