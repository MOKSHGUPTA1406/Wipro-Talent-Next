def main():
    scores = [2, 3, 6, 6, 5]
    
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)
    
    if len(unique_scores) > 1:
        runner_up = unique_scores[1]
        print(runner_up)
    else:
        print("No runner-up score.")

if __name__ == "__main__":
    main()
