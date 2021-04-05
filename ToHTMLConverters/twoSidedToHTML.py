# twoTable = f'''
# <table style = "position: relative;" >
#     <thead>
#         <tr>
#             <td valign="top" style="padding-right: 8px;">
#                 <div style="width: 100%;">
#                     <p class="dp" style="text-align: center">
#                         <span style="font-size: 18px">
#                             <strong>{date1}</strong>
#                         </span>
#                     </p>

#                     <p class="dp" style="text-align: center">
#                         <span style="font-size: 18px; text-align: center">
#                         {description1}
#                         </span>
#                     </p>

#                     {table1}
#                 </div>
#             </td>

#             <td valign="top" style="padding-left: 8px;">
#                 <div style="width: 100%;">
#                     <p class="dp" style="text-align: center">
#                         <span style="font-size: 18px">
#                             <strong>{date2}</strong>
#                         </span>
#                     </p>

#                     <p class="dp" style="text-align: center">
#                         <span style="font-size: 18px; text-align: center">
#                         {description2}
#                         </span>
#                     </p>

#                     {table1}
#                 </div>
#             </td>
#         </tr>
#     </thead>
# </table>
# '''


# songTR = f"""
#     <tr style="border: white;">
# 	    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px; padding-left:12px">{song['composer']}</td>
# 	    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px; padding-left:12px">{song['work']}</td>
# 	    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px; padding-left:12px">{song['performers']}</td>
# 	    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px; padding-left:12px">{song['label']}</td>
# 	    <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px; padding-left:12px">{song['air time']}</td>
#     </tr>
# """


# table = f"""
#     <table class="pp-table-605563f0e749e pp-table-content tablesaw tablesaw-stack datatable" style="width:100%">
# 	    <thead class="tableheader">
# 		    <tr>
# 			    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">Composer</th>
# 			    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">Work</th>
# 			    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">Performers</th>
# 			    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">label</th>
# 			    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">Air Time</th>
# 		    </tr>
# 	    </thead>
# 	<tbody>
# 		{eachTR}
# 	</tbody>
#     </table>
# """

import json
import sys

with open('/Users/shravanp/Coding/FOP/Big-Projects/DrRosen/YearDataJSON/2021.json') as f:
    data = json.load(f)

weeks = data
count = 0
currentArrayValue = 0
TAGBLES = [[]]
for week in weeks:
    if count != 1:
        TAGBLES[currentArrayValue].append(week)
        count += 1
    else:
        TAGBLES[currentArrayValue].append(week)
        count = 0
        currentArrayValue += 1
        TAGBLES.append([])


allTables = ""
currentTagbleUIndex = 0
for splitTagble in TAGBLES:
    if len(splitTagble) == 2:
        week1 = splitTagble[0]
        week2 = splitTagble[1]
        # print(week1)
        # print(week2)
        # print("\n\n\n\n")
        
        date1 = str((week1['date'])).strip()
        description1 = str((week1['description'])).strip()
        date2 = str((week2['date'])).strip()
        description2 = str((week2['description'])).strip()
        # print(date1)
        # print(date2)

        week1SongTRString = ""
        for song in week1['playlist']:
            songTR = f"""
            <tr style="border: white;">
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['composer']}</td>
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['work']}</td>
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['performers']}</td>
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['label']}</td>
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['air time']}</td>
            </tr>
            """
            week1SongTRString = week1SongTRString + " " + songTR

        
        week2SongTRString = ""
        
        for song in week2['playlist']:
            songTR = f"""
            <tr style="border: white;">
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['composer']}</td>
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['work']}</td>
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['performers']}</td>
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['label']}</td>
    	        <td style="border-right: 0.5px solid white; border-top: 1px solid white; border-bottom: 1px solid white; font-size:12px;">{song['air time']}</td>
            </tr>
            """
            week2SongTRString = week2SongTRString + " " + songTR

        table1 = f"""
            <table class="pp-table-605563f0e749e pp-table-content tablesaw tablesaw-stack datatable" style="width:100%">
    	        <thead class="tableheader">
    	    	    <tr>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">Composer</th>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">Work</th>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">Performers</th>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">label</th>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">Air Time</th>
    	    	    </tr>
    	        </thead>
    	        <tbody>
    	        	{week1SongTRString}
    	        </tbody>
                </table>
            """

        table2 = f"""
            <table class="pp-table-605563f0e749e pp-table-content tablesaw tablesaw-stack datatable" style="width:100%">
    	        <thead class="tableheader">
    	    	    <tr>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">Composer</th>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">Work</th>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">Performers</th>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">label</th>
    	    		    <th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; width: auto;">Air Time</th>
    	    	    </tr>
    	        </thead>
    	        <tbody>
    	        	{week2SongTRString}
    	        </tbody>
                </table>
            """

        twoTable = f'''
            <div>
            <table>
            <thead>
                <tr>
                    <td valign="top" style="padding-right: 8px; width: 50%;">
                        <div style="width: 100%;">
                            <p class="dp" style="text-align: center">
                                <span style="font-size: 15px">
                                    <strong>{date1}</strong>
                                </span>
                            </p>

                            <p class="dp" style="text-align: center">
                                <span style="font-size: 15px; text-align: center">
                                {description1}
                                </span>
                            </p>

                            {table1}
                        </div>
                    </td>

                    <td valign="top" style="padding-left: 8px; width: 50%;">
                        <div style="width: 100%;">
                            <p class="dp" style="text-align: center">
                                <span style="font-size: 15px">
                                    <strong>{date2}</strong>
                                </span>
                            </p>

                            <p class="dp" style="text-align: center">
                                <span style="font-size: 15px; text-align: center">
                                {description2}
                                </span>
                            </p>

                            {table2}
                        </div>
                    </td>
                </tr>
            </thead>
            </table>
            </div>
            <br></br>
            '''

        allTables += twoTable
        currentTagbleUIndex += 1
    else:
        playlist = week['playlist']
        date = week['date']
        description = week['description']
    
        dd = f"""
        <br></br>
            <p class="dp" style=" text-align: center;">
        <span style="font-size: 18px;" ><strong>{date}</strong></span>
    </p>
    
    <p class="dp" style=" text-align: center;">
        <span style="font-size: 18px; text-align: center;">{description}</span>
    </p>
        """
    
    
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
    			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">Composer</th>
    			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">Work</th>
    			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">Performers</th>
    			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">label</th>
    			<th style="background-color:#cc6600; color: white; font-size: 12px; font-weight: bold; border-right: 0px solid white;">Air Time</th>		
    		</tr>
    	</thead>
    
    	<tbody>
    		{trstring}
    	</tbody>
    </table>
        """
        tartewas = dd + " " + fulltablestr
        allTables += (tartewas)

print(allTables)
