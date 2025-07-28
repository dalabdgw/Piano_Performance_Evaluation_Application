import pymysql
from dotenv import load_dotenv
import os
import sys
from datetime import datetime


temp_url = ''
url_list = os.getcwd().split('\\')

for i in range(len(url_list)):
    temp_url += f'{url_list[i]}'+'/'

temp_url += 'component_classes/'
print(temp_url)
sys.path.append(temp_url)
from component import User, Song, Review

# Test User Data
testUser = User(
    user_id='ParkMinSeo',
    user_pwd='1234',
    user_name='박민서',
    department='컴퓨터공학과',
    job='학생',
    university='동국대학교',
    ph_num='01073394768',
    created_date='2024-04-03',
    modified_date='2024-04-03'
)

# .env .불러오기
load_dotenv('./database_codes/db_env.env')
database_host = os.getenv('DATABASE_HOST')
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_name = os.getenv('DATABASE_NAME')

print('접속: ', database_host, '유저: ', database_user, '비밀번호: ', database_password, 'DB: ', database_name)


def makeUserTable():
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성

        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
            create table if not exists user(
                user_id varchar(255) primary key,
                user_pwd TEXT not null,
                user_name TEXT not null,
                department varchar(50) not null,
                job varchar(50) not null,
                university TEXT not null,
                ph_num TEXT not null,
                created_date Date not null,
                modified_date Date not null,
                admin int default 0
                );
            """

            # 쿼리 실행
            cursor.execute(create_table_query)

            # 변경사항 저장
            conn.commit()
            print('User Table 생성 완료.')
    except pymysql.Error as e:
        print('User Table 생성 중 오류 발생.')
        print('=' * 50)
        print(e)
        print('=' * 50)
    finally:
        # 데이터베이스 연결 종료
        conn.close()
def makeSongTable():
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
            create table if not exists song(
                song_id int not null auto_increment primary key,
                song_name TEXT not null,
                duration int not null,
                composer TEXT not null
            );
            """

            # 쿼리 실행
            cursor.execute(create_table_query)

            # 변경사항 저장
            conn.commit()
            print('Song Table 생성 완료.')
    except pymysql.Error as e:
        print('Song Table 생성 중 오류 발생')
        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()
def makeSongScoreTable():
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
            create table if not exists song_score(
                song_score_id int not null auto_increment primary key,
                song_id int not null,
                song_part_id int not null unique key,
                sequence int not null,
                song_name TEXT,
                url TEXT not null,
                foreign key song_score1(song_part_id) references song_part(song_part_id),
                foreign key song_score2(song_id) references song(song_id)
            );
            """

            # 쿼리 실행
            cursor.execute(create_table_query)

            # 변경사항 저장
            conn.commit()
            print('Song Score Table 생성 완료.')
    except pymysql.Error as e:
        print('Song Score Table 생성 중 오류 발생')
        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

def makeSongPartTable():
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
           create table if not exists song_part(
            song_part_id int not null auto_increment primary key,
            song_id int not null,
            sequence int not null,
            url TEXT not null,
            is_score int default 0,
            foreign key song_part(song_id) references song(song_id)
        );
            """

            # 쿼리 실행
            cursor.execute(create_table_query)

            # 변경사항 저장
            conn.commit()
            print('Song Part 테이블 생성 완료')
    except pymysql.Error as e:
        print('Song Part 테이블 생성 중 오류 발생.')

        print('=' * 50)
        print(e)
        print('=' * 50)
    finally:
        # 데이터베이스 연결 종료
        conn.close()

def makeReviewTable():
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
            create table if not exists review(
                review_id int not null auto_increment primary key,
                user_id varchar(255) not null,
                created_time Date not null,
                song_id int not null,
                song_part_seq int not null,
                tone_score int not null,
                legato_score int not null,
                representation_score int not null,
                phrasing_score int not null,
                melody_score int not null,
                music_score int not null,
                voicing_score int not null,
                note_score int not null,
                dynamic_score int not null,
                dynamic_change_score int not null,
                tempo_score int not null,
                tempo_change_score int not null,
                articulation_score int not null,
                rhythm_score int not null,
                pedal_score int not null,
                foreign key review(user_id) references user(user_id),
                foreign key review2(song_id) references song(song_id)
                );
            """

            # 쿼리 실행
            cursor.execute(create_table_query)

            # 변경사항 저장
            conn.commit()
            print('Review 테이블 생성 완료.')
    except pymysql.Error as e:
        print('Review 테이블 생성 중 오류 발생.')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

def selectUserId(user_id):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                select user_id from user where user_id = %s
            """

            # 쿼리 실행
            cursor.execute(create_table_query, user_id)

            for id in cursor.fetchall():
                if id[0] == user_id:
                    print('user_id 중복')
                    return 1  # 1 == 이미 존재하는 아이디

            return 0

    except pymysql.Error as e:
        print('user 테이블 조회 중 오류 발생.')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()
def insertUserTable(user: User):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                insert into user(user_id, user_pwd, user_name, department, job, university, ph_num, created_date, modified_date) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """

            # 쿼리 실행
            cursor.execute(create_table_query, user.getInfo())

            # 변경사항 저장
            conn.commit()
            print('새로운 User 생성 완료.')
    except pymysql.Error as e:
        print('회원가입 중 데이터베이스 부분 오류 발생.')

        print('=' * 50)
        print(e)
        print('=' * 50)
        return 1

    finally:
        # 데이터베이스 연결 종료
        conn.close()

    return 0
def getUserPassword(user_id):
    user_pwd = 0
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                select user_pwd from user where user_id = %s
            """

            # 쿼리 실행
            cursor.execute(create_table_query, user_id)

            # 사용자 비밀번호 리턴
            user_pwd = cursor.fetchone()[0]


    except pymysql.Error as e:
        print('사용자 정보 조회 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

    return user_pwd
def getUserAdmin(user_id):
    user_pwd = 0
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                select admin from user where user_id = %s
            """

            # 쿼리 실행
            cursor.execute(create_table_query, user_id)

            # 사용자 비밀번호 리턴
            admin = cursor.fetchone()[0]


    except pymysql.Error as e:
        print('사용자 정보 조회 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

    return admin
def insertSongScoreTable(song_id, score_sequence, score_url, song_part_id):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        print('DB 반영중')
        # 커서 생성
        with conn.cursor() as cursor:

            insert_query = """
                            update song_part set is_score = 1 where song_id = %s and song_part_id = %s
                        """

            cursor.execute(insert_query, (song_id, song_part_id))

            # SQL 쿼리 작성
            insert_query = """
                insert into song_score(song_id, song_part_id, sequence, url) values (%s, %s, %s, %s);
            """

            cursor.execute(insert_query, (song_id, song_part_id, score_sequence, score_url))
            # 변경사항 저장
            conn.commit()

        print('song_score 테이블에 데이터 저장 완료')


        return 0
    except pymysql.Error as e:
        print('곡을 song_score 테이블에 삽입 중 오류 발생.')

        print('=' * 50)
        print(e)
        print('=' * 50)
        return 1

    finally:
        # 데이터베이스 연결 종료
        conn.close()
def insertSongTable(song: Song):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        song_data = song.getSongData()

        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            insert_query = """
                insert into song(song_name, duration, composer) values (%s, %s, %s);
            """

            # 쿼리 실행
            cursor.execute(insert_query, (song_data['song_name'], song_data['duration'], song_data['composer']))

            # 변경사항 저장
            conn.commit()

            select_query = """
                select song_id from song where composer=%s and song_name=%s
            """
            cursor.execute(select_query, (song_data['composer'], song_data['song_name']))
            song_id = cursor.fetchone()[0]

            for i in range(len(song_data['url'])):
                insert_query = """
                    insert into song_part(song_id, sequence, url) values (%s, %s, %s)
                """

                cursor.execute(insert_query, (song_id, song_data['sequence'][i], song_data['url'][i]))
            conn.commit()

        return song_id
    except pymysql.Error as e:
        print('곡을 데이터베이스에 삽입 중 오류 발생.')

        print('=' * 50)
        print(e)
        print('=' * 50)
        return 1

    finally:
        # 데이터베이스 연결 종료
        conn.close()
def getSongData(page_number):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        page_number = int(page_number) * 10
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                    select song_id, song_name, duration, composer from song
                    LIMIT 10 OFFSET %s
                """

            # 쿼리 실행
            cursor.execute(create_table_query, page_number)

            song_name_list = []
            song_duration_list = []
            song_composer_list = []
            song_id_list = []
            for song_data in cursor.fetchall():
                song_id_list.append(song_data[0])
                song_name_list.append(song_data[1])
                song_duration_list.append(song_data[2])
                song_composer_list.append(song_data[3])

        print('곡 정보 조회 완료')

        return song_id_list, song_name_list, song_duration_list, song_composer_list

    except pymysql.Error as e:
        print('곡 정보 불러오는 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()
def getSongPartData(song_id):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                    select song_part_id, sequence, url, is_score from song_part where song_id = %s
                """

            # 쿼리 실행
            cursor.execute(create_table_query, song_id)

            part_url_list = []
            part_sequence_list = []
            is_score_list = []
            song_part_id = []

            for part_data in cursor.fetchall():
                part_url_list.append(part_data[2])
                part_sequence_list.append(part_data[1])
                is_score_list.append(part_data[3])
                song_part_id.append(part_data[0])

        print('곡 파트 정보 불러오기 완료')

        return song_part_id, part_url_list, part_sequence_list, is_score_list

    except pymysql.Error as e:
        print('곡 파트 정보 불러오는 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()
def insertReviewTable(review: Review):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        review_list = review.getReviewDataList()
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d")
        review_list.append(formatted_now)
        print(review_list)
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            insert_query = """
                insert into review(user_id, song_id, song_part_seq, 
                tone_score, legato_score, representation_score, phrasing_score, melody_score,
                 music_score, voicing_score, note_score, dynamic_score,dynamic_change_score,
                  tempo_score, tempo_change_score, articulation_score, rhythm_score, pedal_score, created_time)
                 values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """




            # 쿼리 실행
            cursor.execute(insert_query, review_list)

            # 변경사항 저장
            conn.commit()
            print('평가를 데이터베이스에 삽입 완료')
        return 0
    except pymysql.Error as e:
        print('평가를 데이터베이스에 삽입 중 오류 발생.')

        print('=' * 50)
        print(e)
        print('=' * 50)
        return 1

    finally:
        # 데이터베이스 연결 종료
        conn.close()
def getReviewData(user_id):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        song_name_list = []
        composer_list = []
        duration_list = []
        sequence_list = []
        tone_score_list = []
        legato_score_list = []
        representation_score_list = []
        phrasing_score_list = []
        melody_score_list = []
        music_score_list = []
        voicing_score_list = []
        note_score_list = []
        dynamic_score_list =[]
        dynamic_change_score_list = []
        tempo_score_list =[]
        tempo_change_score_list = []
        articulation_score_list = []
        rhythm_score_list = []
        pedal_score_list = []


        # 커서 생성
        with conn.cursor() as cursor:

            create_table_query = """
                                select song_id from review where user_id = %s
                            """
            cursor.execute(create_table_query, user_id)

            song_id_list = []
            for song_id_data in cursor.fetchall():
                song_id_list.append(song_id_data[0])

            song_id_list = set(song_id_list)

            for song_id in song_id_list:
                # SQL 쿼리 작성
                create_table_query = """select song_part_seq, tone_score, legato_score, representation_score, 
                phrasing_score, melody_score, music_score, voicing_score, note_score, dynamic_score, dynamic_change_score, 
                tempo_score, tempo_change_score, articulation_score, rhythm_score, pedal_score from review where 
                user_id = %s and song_id = %s"""

                # 쿼리 실행
                cursor.execute(create_table_query, (user_id, song_id))

                temp_sequence_list = []
                temp_tone_list = []
                temp_legato_list = []
                temp_representation_list = []
                temp_phrasing_list = []
                temp_melody_list =[]
                temp_music_list = []
                temp_voicing_list = []
                temp_note_list = []
                temp_dynamic_list =[]
                temp_dynamic_change_list = []
                temp_tempo_list= []
                temp_tempo_change_list = []
                temp_articulation_list = []
                temp_rhythm_list =[]
                temp_pedal_list = []

                for review_data in cursor.fetchall():
                    temp_sequence_list.append(review_data[0])
                    temp_tone_list.append(review_data[1])
                    temp_legato_list.append(review_data[2])
                    temp_representation_list.append(review_data[3])
                    temp_phrasing_list.append(review_data[4])
                    temp_melody_list.append(review_data[5])
                    temp_music_list.append((review_data[6]))
                    temp_voicing_list.append(review_data[7])
                    temp_note_list.append(review_data[8])
                    temp_dynamic_list.append(review_data[9])
                    temp_dynamic_change_list.append(review_data[10])
                    temp_tempo_list.append(review_data[11])
                    temp_tempo_change_list.append(review_data[12])
                    temp_articulation_list.append(review_data[13])
                    temp_rhythm_list.append(review_data[14])
                    temp_pedal_list.append(review_data[15])



                sequence_list.append(temp_sequence_list)
                tone_score_list.append(temp_tone_list)
                legato_score_list.append(temp_legato_list)
                representation_score_list.append(temp_representation_list)
                phrasing_score_list.append(temp_phrasing_list)
                melody_score_list.append(temp_melody_list)
                music_score_list.append(temp_music_list)
                voicing_score_list.append(temp_voicing_list)
                note_score_list.append(temp_note_list)
                dynamic_score_list.append(temp_dynamic_list)
                dynamic_change_score_list.append(temp_dynamic_change_list)
                tempo_score_list.append(temp_tempo_list)
                tempo_change_score_list.append(temp_tempo_change_list)
                articulation_score_list.append(temp_articulation_list)
                rhythm_score_list.append(temp_rhythm_list)
                pedal_score_list.append(temp_pedal_list)


                create_table_query2 = """
                                                    select song_name, duration, composer from song where song_id = %s 
                                                """
                cursor.execute(create_table_query2, song_id)

                for temp_song_data in cursor.fetchall():
                    song_name_list.append(temp_song_data[0])
                    duration_list.append(temp_song_data[1])
                    composer_list.append(temp_song_data[2])

        print('리뷰 정보 불러오기 완료')

        return song_name_list, duration_list, composer_list, sequence_list, tone_score_list,legato_score_list,representation_score_list,phrasing_score_list,melody_score_list,music_score_list,voicing_score_list,note_score_list,dynamic_score_list, dynamic_change_score_list, tempo_score_list, tempo_change_score_list, articulation_score_list, rhythm_score_list, pedal_score_list

    except pymysql.Error as e:
        print('리뷰 정보 불러오는 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

def isCheckId(user_id):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        check_user_id = ''
        # 커서 생성
        with conn.cursor() as cursor:

            create_table_query = """
                                select user_id from user where user_id=%s
                            """
            cursor.execute(create_table_query, user_id)

            for i in cursor.fetchall():
                check_user_id = i[0]

        print('아이디 중복체크 확인 완료')
        return check_user_id

    except pymysql.Error as e:
        print('아이디 중복체크 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()
def getReviewByUserIdSongId(song_id, user_id):

    print(song_id, user_id)
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩

        sequence_list = []
        # 커서 생성
        with conn.cursor() as cursor:

            create_table_query = """
                                select song_part_seq from review where user_id=%s and song_id=%s
                            """
            cursor.execute(create_table_query, (user_id, song_id))

            for i in cursor.fetchall():
                print(i)
                sequence_list.append(i[0])

        print('평가 정보 확인 완료')
        return sequence_list

    except pymysql.Error as e:
        print('평가 정보 확인 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

def getSongScoreData(song_id, song_part_id):
    """
    데이터베이스에서 곡 악보를 가져오는 함수
    :param song_id: 데이터베이스 속 곡 id
    :param song_part_id: 데이터베이스 속 곡 파트 id
    :return: 곡 악보 정보
    """
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                    select sequence, url from song_score where song_name=%s and sequence=%s
                """


#start

            # 쿼리 실행
            cursor.execute(create_table_query, (song_id, song_part_id))

            sequence = []
            score_url_list = []
            
            for song_data in cursor.fetchall():
                sequence.append(song_data[0])
                score_url_list.append(song_data[1])
                
        print('곡 악보 정보 조회 완료')

        return sequence, score_url_list
    

    except pymysql.Error as e:
        print('곡 악보 정보 불러오는 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()


def getSearchData(search_text):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                    select * from song where song_name LIKE %s
                """
            print(search_text)
            like_pattern = '%'+search_text+'%'
            # 쿼리 실행
            cursor.execute(create_table_query, (like_pattern),)

            song_id_list = []
            song_name_list = []
            song_duration_list = []
            song_composer_list = []

            for song_data in cursor.fetchall():
                song_id_list.append(song_data[0])
                song_name_list.append(song_data[1])
                song_duration_list.append(song_data[2])
                song_composer_list.append(song_data[3])
                print(song_data)
        print('곡 검색 조회 완료')

        return song_id_list, song_name_list, song_duration_list, song_composer_list


    except pymysql.Error as e:
        print('곡 악보 정보 불러오는 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

def getUserName(user_id):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                    select user_name from user where user_id=%s
                """
            # 쿼리 실행
            cursor.execute(create_table_query, user_id)

            user_name = ''

            for song_data in cursor.fetchall():
                user_name = song_data[0]
        print('유저 이름 조회 완료')

        return user_name


    except pymysql.Error as e:
        print('유저 이름 정보 불러오는 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

def deleteScore(song_part_id, song_id):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                    delete from song_score where song_part_id=%s and song_id=%s
                """
            # 쿼리 실행
            cursor.execute(create_table_query, (song_part_id, song_id))

            create_table_query = """
                   update song_part set is_score=0 where song_part_id=%s and song_id=%s
                """

            cursor.execute(create_table_query, (song_part_id, song_id))

            conn.commit()
        print('악보 삭제 완료')




    except pymysql.Error as e:
        print('악보 삭제 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

def deleteReviewByUserId(user_id, song_part_id, song_name):
    try:
        # MySQL 데이터베이스에 연결
        conn = pymysql.connect(
            host=database_host,  # 데이터베이스 호스트 주소
            user=database_user,  # 데이터베이스 사용자 이름
            password=database_password,  # 데이터베이스 패스워드
            database=database_name,  # 데이터베이스 이름
            charset='utf8mb4')  # 문자 인코딩
        # 커서 생성
        with conn.cursor() as cursor:
            # SQL 쿼리 작성
            create_table_query = """
                                select song_id from song where song_name=%s
                            """

            cursor.execute(create_table_query, song_name)



            song_id = " "
            for song_data in cursor.fetchall():
                song_id = song_data[0]


            create_table_query = """
                    delete from review where song_part_seq=%s and song_id=%s and user_id=%s
                """
            # 쿼리 실행
            cursor.execute(create_table_query, (song_part_id, song_id, user_id))

            conn.commit()
        print('리뷰 정보 삭제 완료')




    except pymysql.Error as e:
        print('리뷰 정보 삭제 중 오류 발생')

        print('=' * 50)
        print(e)
        print('=' * 50)

    finally:
        # 데이터베이스 연결 종료
        conn.close()

