from inference import predict_priority

if __name__ == "__main__":
    subject = "Server is down for multiple users"
    body = "Our main production server has been unreachable for 30 minutes. Customers cannot log in."
    label, score = predict_priority(subject, body)
    print("Predicted priority:", label)
    print("Confidence:", score)
