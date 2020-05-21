Q1 = '''SELECT mc.captain, mc.team_id,p.jersey_no,p.name,p.date_of_birth,p.age from Player AS p
        INNER JOIN MatchCaptain mc on mc.captain = p.player_id
        WHERE EXISTS(SELECT mc.captain FROM MatchCaptain mc WHERE mc.captain = p.player_id)
        AND NOT EXISTS(SELECT goal_id FROM GoalDetails gd WHERE gd.player_id = p.player_id)''';
        
        
Q2 =  '''SELECT team_id,(select count(match_n) from MatchTeamDetails where mt.team_id = MatchTeamDetails.team_id) as no_of_games 
         from MatchTeamDetails as mt GROUP BY mt.team_id''';
         
         
Q3 = '''SELECT gd.team_id, 
        ((select count(goal_id) from GoalDetails where GoalDetails.team_id = t.team_id )/
        CAST((select count(p.player_id) from player p where p.team_id = t.team_id)AS FLOAT))
        average_goal_score from GoalDetails as gd
        INNER JOIN Team as t on t.team_id = gd.team_id
        GROUP BY gd.team_id''';
        
Q4 = '''SELECT captain, (select count(captain) from MatchCaptain mc1 where mc1.captain = p.player_id) as
        no_of_times_captain from MatchCaptain as mc
        INNER JOIN Player p ON p.player_id = mc.captain
        GROUP BY p.player_id''';    
        
Q5 = '''SELECT COUNT(DISTINCT(m.player_of_match)) from match as m
        INNER JOIN MatchCaptain mc ON mc.captain = m.player_of_match  AND m.match_no = mc.match_no''';
        
        
Q6 = '''SELECT DISTINCT(player_id) from player as p
        WHERE EXISTS (SELECT mc.captain from  MatchCaptain AS mc where mc.captain = p.player_id)
        and not exists(select player_of_match from match where match.player_of_match = p.player_id)
        ''';
        
Q7 = '''SELECT strftime("%m", play_date) as month,
        (SELECT COUNT(m.match_no) from Match m 
        WHERE strftime("%m",m.play_date) = strftime("%m",`Match`.play_date)) as no_of_matches FROM Match
        GROUP BY month ORDER BY no_of_matches DESC''';

        
Q8 =  '''SELECT jersey_no, count(mc.captain)no_captains from player p 
         INNER JOIN MatchCaptain mc ON mc.captain = p.player_id
         GROUP BY jersey_no ORDER BY no_captains DESC,jersey_no DESC''';
 
Q9 = '''SELECT p.player_id, AVG(m.audience) as avg_audience from player p
        INNER JOIN MatchTeamDetails mt ON mt.team_id = p.team_id
        INNER JOIN Match m on mt.match_no = m.match_no
        GROUP BY p.player_id ORDER BY avg_audience DESC, p.player_id DESC''';        
        
Q10 = '''SELECT team_id,(SELECT AVG(age) from player p where p.team_id = player.team_id) 
         from player GROUP BY team_id''';
         
Q11= '''SELECT AVG(age) from player p 
        INNER JOIN MatchCaptain mc on mc.captain = p.player_id''';
        
Q12 = '''SELECT strftime("%m",date_of_birth) as month, (select count(p.player_id) 
         from player p where strftime("%m", `player`.date_of_birth) = strftime("%m",p.date_of_birth)) as no_of_players from player
         GROUP BY month ORDER BY no_of_players DESC, month DESC''';      

Q13 = '''SELECT captain, count(win_lose) as no_of_wins from MatchCaptain mc
         INNER JOIN MatchTeamDetails mt on mc.match_no = mt.match_no and mc.team_id = mt.team_id
         WHERE win_lose = 'W'  GROUP BY captain
         ORDER BY no_of_wins DESC''';
        
        
        