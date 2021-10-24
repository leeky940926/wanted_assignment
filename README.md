| Index  | Http Method |  URI            |  Description    |  Request variable  |  Response Status Code   | 작업 브랜치
|:--------:|:-----------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|
| 1 |  POST | /users/signup | 회원가입(비밀번호 암호화,</br>이메일과 비밀번호 정규식 작성)  | email, password, phone_number, name  | 201 | feature/signup
| 2 |  POST | /users/signin | 로그인(토큰 발행)  | email, password  | 201 | feature/signin
| 3 |  POST | /postings | 게시글 작성 | title, content, user_id</br>(유저 고유ID는 토큰으로 식별)  | 201 | feature/postings-c
| 4 |  GET | /postings | 게시글 조회</br>(offset과 limit을 이용한 Pagination구현 | 없음  | 200 | feature/posting-r
| 5 |  PATCH | /postings/{posting_id} | 게시글 수정 | posting_id  | 201 | feature/posting-u
| 6 |  DELETE | /postings/{posting_id} | 게시글 삭제 | posting_id  | 201 | feature/posting-d
