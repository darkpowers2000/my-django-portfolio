def analyze_customer_sentiment(review_string):
    positive_flags = ["excellent", "saved", "fast", "incredible", "efficient", "love"]
    negative_flags = ["slow", "broken", "dropped", "error", "failed", "expensive"]
    
    score = 0
    words = review_string.lower().split()
    
    for word in words:
        if word in positive_flags: score += 1
        if word in negative_flags: score -= 1
        
    sentiment = "NEUTRAL"
    if score > 0: sentiment = "POSITIVE"
    elif score < 0: sentiment = "NEGATIVE"
    
    return {"raw_review": review_string, "calculated_sentiment": sentiment, "magnitude": score}

if __name__ == "__main__":
    test_string = "Your automated software pipeline is excellent and fast, it saved our operations department hours."
    print("[+] Sentiment analysis text engine execution complete:")
    print(analyze_customer_sentiment(test_string))