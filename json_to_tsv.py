import json
import pandas as pd


if __name__ == "__main__":
    with open('reviews.json', 'r') as fp:
        reviews = json.load(fp)
        data_matrix = []

        for review in reviews:
            data_matrix.append([review['id'], review['data'], review['label']])

        df = pd.DataFrame(data=data_matrix, columns=['Id', 'Review', 'Label'])
        df.to_csv('reviews.tsv', sep='\t', index=False)

    with open('reviews_by_course.json', 'r') as fp:
        reviews_by_course = json.load(fp)
        data_matrix = []

        for course_reviews in reviews_by_course:
            for i in range(len(course_reviews['data'])):
                data_matrix.append([course_reviews['id'], course_reviews['data'][i], course_reviews['ratings'][i]])

        df = pd.DataFrame(data=data_matrix, columns=['CourseId', 'Review', 'Label'])
        df.to_csv('reviews_by_course.tsv', sep='\t', index=False)

