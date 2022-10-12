import speedtest

try:
    print("\nYour Download and Upload Speed is Testing...\n")

    st = speedtest.Speedtest()

    download_speed_mbps = round(st.download() / (10**6), 2)
    upload_speed_mbps = round(st.upload() / (10**6), 2)

    print(f"Download Speed : {download_speed_mbps} Mbps")
    print(f"Upload Speed : {upload_speed_mbps} Mbps\n")
except:
    print("Test Failed!")
    print("There is an Problem in Testing. PLease Check Your Internet Connectivity & Try Again!")
