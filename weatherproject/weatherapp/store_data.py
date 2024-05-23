import sys
import os
import django
import pandas as pd


def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.abspath(os.path.join(script_dir, "../"))
    sys.path.append(project_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weatherproject.settings")
    django.setup()

    from weatherapp.models import City

    def store_data():
        csv_file_path = os.path.join(script_dir, "data_manipulation", "cities.csv")

        if not os.path.isfile(csv_file_path):
            return

        df = pd.read_csv(csv_file_path)

        if df.empty:
            return

        for index, row in df.iterrows():
            obj, created = City.objects.get_or_create(
                city_name=row["name"],
                country_name=row["country"],
                longitude=row["lon"],
                latitude=row["lat"],
            )

    store_data()


if __name__ == "__main__":
    main()
