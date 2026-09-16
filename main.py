from datetime import datetime
from operations import Operation


def main():

    operate = Operation(5, 2, 5)
    print("---Sensor Event Processing System---")

    try:
        while True:
            print("\n1. Create event")
            print("2. Display queued events")
            print("3. Process event")
            print("4. Display Recent Readings")
            print("5. Display Recovery Stack")
            print("6. Exit")

            op = input("Choose option: ")

            if op == "1":
                try:
                    print("\n---Add the event---")
                    sensor_id = input("Enter sensor id: ")
                    value = float(input("Enter value: "))
                    timestamp = datetime.now()
                    data = operate.create_event(sensor_id, value, timestamp)
                    print(data)
                except OverflowError as e:
                    print(f"Event addition error: {e}")
            elif op == "2":
                try:
                    events = operate.display_events()
                    for event in events:
                        print(
                            f"Event - {event.event_id} | {event.sensor_id} | {event.value} | {event.timestamp}")
                except OverflowError as e:
                    print(f"Display error: {e}")
            elif op == "3":
                try:
                    print(operate.process_event())
                except (IndexError, OverflowError) as e:
                    print(f"Processign failed: {e}")
            elif op == "4":
                try:
                    events = operate.current_reading()
                    for event in events:
                        print(f"Current readings: {event}")
                except (IndexError, OverflowError) as e:
                    print(f"Readings error: {e}")

            elif op == "5":
                try:
                    event = operate.recovery_stack()
                    print(event)
                except (IndexError, OverflowError) as e:
                    print(f"Recovery error: {e}")

            elif op == "6":
                print("\nThank you\n")
                break
            else:
                print("Invalid option")
    finally:
        operate.database.close()


if __name__ == "__main__":
    main()
