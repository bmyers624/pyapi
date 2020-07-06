#!/usr/bin/python3
"""Russel Zachary Feeser Using etcd to design a RESTful ticket server"""

import requests

ETCD = "http://127.0.0.1:2379/v2/keys/tickets"

def gettickets():
    resp = requests.get(ETCD)
    resp = resp.json()

    if resp.get("errorCode"):
        return False
    else:
        ticketlist = []
        if resp.get("node").get("nodes"):
            for ticket in resp.get("node").get("nodes"):
                ticketlist.append(ticket.get("key").lstrip("/tickets/"))
            return ticketlist
        else:
            return False

def getoneticket(ticketid):
    resp = requests.get(f"{ETCD}/{ticketid}")
    resp = resp.json

    if resp.get("errorCode"):
        return False
    else:
        return resp.get("node").get("value")

def createticket(descofissue):
    resp = requests.post(ETCD, data={'value': descofissue })
    resp = resp.json()

    resp = resp.get("node").get("key").lstrip("/tickets/")
    return resp

def updateticket(ticketid, descofissue):
    if getoneticket(ticketid):
        resp = requests.put(f"{ETCD}/{ticketid}", data={'value': descofissue })
        resp = resp.json()
    else:
        return False
    return (resp.get("node").get("value"), resp.get("prevNode").get("value"))

def deleteticket(ticketid):
    requests.delete(f"{ETCD}/{ticketid}")
    return

def deletealltickets():
    requests.delete(f"{ETCD}?dir=true&recursive=true")
    return

def main():
    while True:
        print("""
        1) Read all available tickets
        2) Get ticket
        3) Create ticket
        4) Update ticket
        5) Delete ticket
        6) Exit
        99) DANGER! Delete all tickets
        """)

        userinput = ""
        while userinput == "": 
            userinput = input("> ")

        if userinput == "1":
            ticketlist = gettickets()
            if ticketlist:
                print()
                for ticket in ticketlist:
                    print(f"Ticket ID - {ticket}")
            else:
                print("There are no tickets in the system")

        elif userinput == "2":
            ticketid = input("What is the ticket ID? ")
            oneticket = getoneticket(ticketid)
            # if oneticket returns a string or FALSE
            if oneticket:
                print(f"\nFor {ticketid}:")
                print(f"    Ticket Descripition - {oneticket}")
            ## handles condition where FALSE is returned
            else:
                print("That ticket does not exist within the system.")

        ## user wants to create a ticket
        elif userinput == "3":
            descofissue = input("Give a short 140 char description of the issue: ")
            createdticket = createticket(descofissue)
            print(f"\nTicket {createdticket} has been created.")

        ## user wants to update a ticket
        elif userinput == "4":
            ticketid = input("Update what ticket ID? ")
            descofissue = input("What is the updated 140 char description of the issue: ")
            ## updatedticket returns a two-tuple, or FALSE
            updatedticket = updateticket(ticketid, descofissue)
            if updatedticket:
                print(f"\nFor {ticketid}:")
                print(f"    Updated Ticket Description - {updatedticket[0]}")
                print(f"    Old Ticket Description - {updatedticket[1]}")
            else: ## if updatedticket() returned FALSE
                print("That ticket does not exist within the system.")

        ## user wants to delete a ticket
        elif userinput == "5":
            ticketid = input("What is the ticket ID? ")
            deleteticket(ticketid)
            print(f"\nTicket {ticketid} has been removed from the system")

        ## user wants to exit
        elif userinput == "6":
            ## end the while True loop
            break

        elif userinput == "99":
            deletealltickets()
            print("All tickets have been removed from the system")

        ## user inputs a non valid option
        else:
            print("That is not a valid option")

    print("Thanks for using the Alta3 RESTful ticketing service")

if __name__ == "__main__":
    main()
