# 단어 표시 프로그램

---

## 소개

이 프로그램은 사용자가 입력한 단어를 시간 간격에 맞춰 화면에 표시하는 웹 애플리케이션입니다. PDF 파일을 업로드하여 해당 파일에 있는 단어를 추출하거나 직접 텍스트를 입력하여 사용할 수 있습니다. 사용자는 시작, 일시정지, 재개 버튼을 통해 단어 표시를 제어할 수 있으며, 표시되는 단어의 글꼴 크기와 색상을 선택할 수 있습니다.

---

## 사용 방법

1. **PDF 업로드**: PDF 파일을 선택하여 업로드합니다. 업로드한 PDF 파일에서 단어를 추출하여 화면에 표시합니다.
2. **텍스트 입력**: 직접 텍스트를 입력하여 사용할 수도 있습니다. 텍스트를 입력할 텍스트 영역에 단어를 입력하면 자동으로 단어를 인식하여 표시합니다.
3. **시간 설정**: 단어 간의 표시 간격을 조절할 수 있습니다. 시간을 설정하는 슬라이더를 조작하여 간격을 변경할 수 있습니다.
4. **표시 제어**: 시작하기, 일시정지, 재개 버튼을 사용하여 단어의 표시를 제어할 수 있습니다.
5. **글꼴 크기 및 색상 변경**: 표시되는 단어의 글꼴 크기와 색상을 변경할 수 있습니다. 선택한 글꼴 크기와 색상은 즉시 적용됩니다.

---

## 주의 사항

- PDF 파일을 업로드할 때는 반드시 PDF 형식의 파일을 선택해야 합니다.
- 텍스트 입력 시에는 공백을 기준으로 단어를 구분합니다.
- 시간 간격은 밀리초 단위로 설정됩니다. 최소 100밀리초부터 최대 1000밀리초까지 조절할 수 있습니다.
- 시작하기 버튼을 누를 때마다 새로운 단어 표시가 시작됩니다. 일시정지 후에는 다시 시작하기를 눌러야 표시가 재개됩니다.

---

## 개발 환경

- 이 애플리케이션은 HTML, CSS, JavaScript로 개발되었습니다.
- PDF 파일의 처리를 위해 `pdf.js` 라이브러리를 사용하였습니다.

---

## 라이선스

이 프로그램은 MIT 라이선스 하에 배포됩니다.

---

## 문의

질문이나 제안이 있으시면 010-5635-3849로 문의해주세요.

---

## 버전 기록

- v1.0 (YYYY년 MM월 DD일): 초기 버전 배포.
