public class Producer implements Runnable {


    private final ArrayBlockingQueue<Path> filelist;
    private final Path path;


    public Producer(ArrayBlockingQueue<Path> filelist,Path path){
        this.filelist = filelist;
        this.path = path;
    }

    @Override
    public void run() {
        try {
            Files.walkFileTree(this.path,new SimpleFileVisitor<Path>(){
                @Override
                public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                    try {
                        filelist.put(file);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    return FileVisitResult.CONTINUE;
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public ArrayBlockingQueue<Path> getFilelist() {
        return filelist;
    }
}
