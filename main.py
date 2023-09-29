import os
import re
import json
import shutil
import logging
from datetime import datetime, timedelta
from dateutil import parser


class LogArchiver:
    def __init__(self, settings_file):
        with open(settings_file, 'r') as json_file:
            data = json.load(json_file)

        self.file_paths = data['path']
        self.days_to_subtract = data['days_to_subtract']

        logging.basicConfig(filename='logarchiver.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def path_exists(self, path):
        return os.path.exists(path)

    def move_logs_to_archive(self, path):
        files = os.listdir(path)
        date_filter = re.compile(r'\d{8}|\d{2,4}-\d{2}-\d{2,4}')
        current_date = datetime.now().date()

        for file in files:
            try:

                found_date = date_filter.search(file)

                if found_date:
                    found_date = found_date.group()
                    date = parser.parse(found_date).date()

                    if date < current_date:
                        shutil.move(os.path.join(path, file), os.path.join(self.archive_path, file))
                        logging.info(f'moved file:{file} to archive folder')

            except Exception as e:
                logging.error(f'Exception found on {file}: {e}')
            
            logging.info('archive process complete!')

    def delete_older_log_files(self):
        files = os.listdir(self.archive_path)
        date_filter = re.compile(r'\d{8}|\d{2,4}-\d{2}-\d{2,4}')
        end_date = (datetime.now() - timedelta(days=self.days_to_subtract)).date()

        logging.info(f'deleting files older than {end_date}')

        for file in files:
            found_date = date_filter.search(file)

            if found_date:
                found_date = found_date.group()
                date = parser.parse(found_date).date()

                if date <= end_date:
                    os.remove(os.path.join(self.archive_path, file))
                    logging.info(f'file was deleted {os.path.join(self.archive_path, file)}')

    def archive_logs(self):
        for path in self.file_paths:
            self.archive_path = os.path.join(path, 'archive')

            logging.info(f'archive logs on {path}')

            if not self.path_exists(self.archive_path):
                os.mkdir(self.archive_path)
                logging.info(f'archive path was created {self.archive_path}')

            self.move_logs_to_archive(path)
            self.delete_older_log_files()


if __name__ == "__main__":
    log_archiver = LogArchiver('settings.json')
    log_archiver.archive_logs()
