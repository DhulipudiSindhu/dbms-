Q1 = '''SELECT a.id, a.fname, a.lname, a.gender from Actor as a 
        inner join cast ON `cast`.pid = a.id
        INNER JOIN Movie m on `cast`.mid = m.id
        WHERE m.name LIKE 'Annie%' ''';
        
Q2 = '''SELECT m.id,m.name,m.rank,m.year from movie as m
        INNER JOIN MovieDirector md on md.mid = m.id
        INNER JOIN Director d on d.id = md.did
        where d.fname = 'Biff' and lname = 'Malibu' and year IN (1999, 1994,2003)
        ORDER BY rank DESC, year ASC''';
        
Q3 = '''SELECT m.year,COUNT(m.name) from movie as m GROUP BY m.year
        HAVING (SELECT AVG(rank) from movie where `movie`.year = m.year) >
        (SELECT AVG(rank) from movie) ORDER BY m.year ASC''';
        
Q4 = '''SELECT m.id, m.name,m.year, m.rank from movie m 
        WHERE m.year = 2001 and rank < (select AVG(rank) from movie WHERE year = 2001)
        order by m.rank DESC limit 10 offset 0''';
  

Q5 = '''SELECT m.id as movie_id,
        (select count(a.gender) from Actor a INNER JOIN cast c on c.pid = a.id where c.mid = m.id and a.gender = 'F') as no_of_female_actors,
        (select count(a.gender) from Actor a INNER JOIN cast c on c.pid = a.id where c.mid = m.id and a.gender = 'M') as no_of_male_actors
         FROM Movie m ORDER BY m.id ASC LIMIT 100 OFFSET 0''';
         
Q6 = '''SELECT c.pid from Cast c
        INNER JOIN Movie m ON m.id = c.mid
        INNER JOIN Actor a ON a.id = c.pid
        Group by c.pid,c.mid having count(distinct role) > 1
        ORDER BY a.id ASC LIMIT 100
        ''';
        
Q7 = '''SELECT fname, count(fname) 
        from director GROUP BY fname HAVING COUNT(fname) > 1
        ''';
        
Q8 = '''SELECT d.id, d.fname, d.lname from director d
        WHERE EXISTS (select c.pid from cast c INNER JOIN MovieDirector md on c.mid = md.mid
        where d.id = did GROUP BY c.mid HAVING COUNT(DISTINCT c.pid) >= 100)
        AND NOT EXISTS(select c.pid from cast c INNER JOIN MovieDirector md ON c.mid = md.mid 
        where d.id = did GROUP BY c.mid HAVING COUNT(DISTINCT c.pid)<100)''';
         