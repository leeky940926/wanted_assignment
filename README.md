안녕하세요.

위코드 25기로 이번 과정에 참여하게된 이기용입니다.

해당 README.md 파일은 두 가지 목차로 이루어져 있습니다.

1. API명세
각 API에 대해 표로 정리를 했으며, 구성은 HTTP Method / URI / Description / Request Variable / Response Status Code / Branch 입니다.

2. 추가 상세 설명
이 부분은 제가 직접 구현한 코드에 대해 어떤 생각을 가지고 작성했는지 기술되어 있습니다.

<br>

| Index  | Http Method |  URI            |  Description    |  Request variable  |  Response Status Code   | Branch
|:--------:|:-----------:|:----------------:|:----------------:|:----------------:|:----------------:|:------------------------:|
| 1 |  POST | /users/signup | 회원가입</br>(비밀번호 암호화,이메일과 </br>비밀번호 정규식</br>작성)  | email, password  | 201 | feature/signup
| 2 |  POST | /users/signin | 로그인(토큰 발행)  | email, password  | 201 | feature/signin
| 3 |  POST | /postings | 게시글 작성 | title, content, user_id</br>(유저 고유ID는 토큰으로</br>식별)  | 201 | feature/postings-c
| 4 |  GET | /postings | 게시글 조회</br>(offset과 limit을 </br>이용한 Pagination구현 | 없음  | 200 | feature/postings-r
| 5 |  PATCH | /postings/{posting_id} | 게시글 수정 | posting_id  | 201 | feature/postings-u
| 6 |  DELETE | /postings/{posting_id} | 게시글 삭제 | posting_id  | 201 | feature/postings-d

