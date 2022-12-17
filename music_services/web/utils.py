def return_valid_avg_score(total_score, scores_count):
    if scores_count > 0:
        avg_score = total_score / scores_count
        return avg_score

    return None


def calc_avg_review_score(reviews):
    total_score = 0
    scores_count = 0

    for r in reviews:
        total_score += r.rating
        scores_count += 1

    avg_score = return_valid_avg_score(total_score, scores_count)

    return avg_score

