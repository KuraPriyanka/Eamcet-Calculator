import requests
from bs4 import BeautifulSoup
def score_calculator(soup):
    questions = []
    for question in soup.find_all("div", class_="question-pnl"):
        questions.append(question)
    score = 0

    for question in questions:
        correct_option = int(question.find("td", class_="rightAns").text[0])
        
        # Assuming 'question' is your BeautifulSoup object
        td_elements = question.find_all("td", class_="bold")
        if td_elements:
            last_td_text = td_elements[-1].text
        # Convert the text to an integer
            try:
                chosen_option = int(last_td_text)
                # Use chosen_option as needed
            except ValueError:
                score += 0
        else:
            print("No td elements with class 'bold' found.")

        if correct_option == chosen_option:
            score += 1
   
    return score


def process_link(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    maths_score = 0
    physics_score = 0
    chemistry_score = 0
    total_score = 0
    name = ""
    hall_ticket_number = ""

    for section_cntr in soup.find_all("div", class_="section-cntnr"):
        section_span = section_cntr.find("div", class_="section-lbl")
        if section_span:
            section_text = section_span.find("span", class_="bold").text
            if section_text == "Physics":
                physics_score += score_calculator(section_cntr)
            elif section_text == "Mathematics":
                maths_score += score_calculator(section_cntr)
            else:
                chemistry_score += score_calculator(section_cntr)

    total_score = maths_score + physics_score + chemistry_score
    target_name = soup.find("td", text="Hall Ticket Number")
    hall_ticket_number = target_name.find_next_sibling().text
    target_hall_ticket = soup.find("td", text="Candidate Name")
    name = target_hall_ticket.find_next_sibling().text

    return [name, hall_ticket_number, maths_score, physics_score, chemistry_score, total_score]
