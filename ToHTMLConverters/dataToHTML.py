import sys
import json

with open(f'/Users/shravanp/Coding/FOP/Big-Projects/DrRosen/YearDataJSON/2021.json') as f:
    data = json.load(f)

month = str("January")

for week in data:

    playlist = week['playlist']
    date = week['date']
    description = week['description']

    if "INTERNATIONAL EDITION - LIVE FROM HOME WPRB RADIO BROADCAST" in description:
        description = description.replace(
            "INTERNATIONAL EDITION - LIVE FROM HOME WPRB RADIO BROADCAST", "")
        description = description + """
        <p class="dp" style=" text-align: center;">
    <span style="font-size: 18px; text-align: center;">INTERNATIONAL EDITION - LIVE FROM HOME WPRB RADIO BROADCAST</span>
</p>
      """
    if str(month) in str(date):
        pass
    else:
        continue

    dd = f"""
    <br></br>
        <p class="dp" style=" text-align: center;">
    <span style="font-size: 18px;" ><strong>{date}</strong></span>
</p>

<p class="dp" style=" text-align: center;">
    <span style="font-size: 18px; text-align: center;">{description}</span>
</p>
    """

    print(dd)

    row = 1
    trs = []
    trstring = ""
    for song in playlist:
        tr = f"""
            <tr style="border: white;">
		    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:13px; padding-left:10px">{song['composer']}</td>
		    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:13px; padding-left:10px">{song['work']}</td>
		    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:13px; padding-left:10px">{song['performers']}</td>
		    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:13px; padding-left:10px">{song['label']}</td>
		    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:13px; padding-left:10px">{song['air time']}</td>
            """

        trs.append(tr)
        row += 1

    for xtr in trs:
        trstring = trstring + " " + str(xtr)
    fulltablestr = f"""
                    <table class="pp-table-605563f0e749e pp-table-content tablesaw tablesaw-stack datatable" style="width:100%">
	<thead class="tableheader">
		<tr>
			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white; padding-left:10px; padding-top:8px; padding-bottom:8px">Composer</th>
			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white; padding-left:10px; padding-top:8px; padding-bottom:8px">Work</th>
			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white; padding-left:10px; padding-top:8px; padding-bottom:8px">Performers</th>
			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white; padding-left:10px; padding-top:8px; padding-bottom:8px">label</th>
			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white; padding-left:10px; padding-top:8px; padding-bottom:8px">Air Time</th>		
		</tr>
	</thead>
	
	<tbody>
		{trstring}
	</tbody>
</table>
    """
    print(fulltablestr)
