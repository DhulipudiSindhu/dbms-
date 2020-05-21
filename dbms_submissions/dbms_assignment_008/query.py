Q1 = '''SELECT d.id, d.fname FROM Director AS d WHERE
        EXISTS(SELECT md.did FROM MovieDirector AS md INNER JOIN Movie on md.mid = movie.id
        WHERE d.id = md.did AND Movie.year > 2000) AND
        NOT EXISTS(SELECT md.did FROM MovieDirector AS md INNER JOIN Movie on md.mid = Movie.id
        WHERE d.id = md.did AND Movie.year < 2000) ORDER BY d.id ASC''';
        
        
Q2 ='''SELECT fname,
        (SELECT name FROM Movie 
        INNER JOIN MovieDirector as md ON md.mid = Movie.id
        WHERE d.id = md.did ORDER BY rank desc,name ASC LIMIT 1)
        FROM Director as d limit 100
      ''';  

 
Q3 = '''
     SELECT * from Actor as a WHERE 
     NOT EXISTS(SELECT pid from cast as c INNER JOIN Movie ON Movie.id = c.mid
     WHERE a.id = c.pid AND year BETWEEN 1990 AND 2000) ORDER BY a.id DESC LIMIT 100
     ''';
     
     